package model.statement;

import exceptions.MyException;
import model.adt.MyIDictionary;
import exceptions.StatementExecutionException;
import model.expression.Expression;
import model.state.Heap;
import model.state.ProgramState;
import model.state.SymbolTable;
import model.type.RefType;
import model.type.Type;
import model.value.RefValue;
import model.value.Value;

public record HeapWriteStatement(String varName, Expression expression) implements Statement {

    @Override
    public ProgramState execute(ProgramState state) {
        SymbolTable sym = state.symbolTable();
        Heap heap = state.heap();

        if (!sym.isDefined(varName)) {
            throw new StatementExecutionException("wH: variable '" + varName + "' is not defined");
        }

        Value varVal = sym.getValue(varName);
        if (!(varVal instanceof RefValue refValue)) {
            throw new StatementExecutionException("wH: variable '" + varName + "' is not a RefValue");
        }

        int address = refValue.getAddress();
        if (!heap.isDefined(address)) {
            throw new StatementExecutionException("wH: address " + address + " is not in the heap");
        }

        Value eval = expression.evaluate(sym, heap);
        if (!eval.getType().equals(refValue.getLocationType())) {
            throw new StatementExecutionException("wH: type mismatch for variable '" + varName + "'");
        }

        heap.update(address, eval);
        return null;
    }

    @Override
    public MyIDictionary<String, Type> typecheck(MyIDictionary<String, Type> typeEnv) throws MyException {
        Type typevar = typeEnv.lookup(varName);
        if (!(typevar instanceof RefType refType)) {
            throw new MyException("wH: variable '" + varName + "' is not a RefType");
        }
        Type typexp = expression.typecheck(typeEnv);
        if (!refType.getInner().equals(typexp)) {
            throw new MyException("wH: right hand side and left hand side have different types");
        }
        return typeEnv;
    }

    @Override
    public String toString() {
        return "wH(" + varName + ", " + expression + ")";
    }
}
