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

public record HeapAllocationStatement(String varName, Expression expression) implements Statement {

    @Override
    public ProgramState execute(ProgramState state) {
        SymbolTable sym = state.symbolTable();
        Heap heap = state.heap();

        if (!sym.isDefined(varName)) {
            throw new StatementExecutionException("new: variable '" + varName + "' is not defined");
        }

        Value varVal = sym.getValue(varName);
        if (!(varVal.getType() instanceof RefType refType)) {
            throw new StatementExecutionException("new: variable '" + varName + "' is not a RefType");
        }

        Value eval = expression.evaluate(sym, heap);
        Type locationType = refType.getInner();
        if (!eval.getType().equals(locationType)) {
            throw new StatementExecutionException("new: type mismatch for variable '" + varName + "'");
        }

        int address = heap.allocate(eval);
        sym.update(varName, new RefValue(address, locationType));

        return null;
    }

    @Override
    public MyIDictionary<String, Type> typecheck(MyIDictionary<String, Type> typeEnv) throws MyException {
        Type typevar = typeEnv.lookup(varName);
        Type typexp = expression.typecheck(typeEnv);
        if (typevar.equals(new RefType(typexp))) {
            return typeEnv;
        }
        throw new MyException("NEW stmt: right hand side and left hand side have different types");
    }

    @Override
    public String toString() {
        return "new(" + varName + ", " + expression + ")";
    }
}
