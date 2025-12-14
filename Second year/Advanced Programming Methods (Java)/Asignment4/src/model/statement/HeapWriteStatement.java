package model.statement;

import model.expression.Expression;
import model.state.Heap;
import model.state.ProgramState;
import model.state.SymbolTable;
import model.value.RefValue;
import model.value.Value;
import exceptions.StatementExecutionException;

public record HeapWriteStatement(String varName, Expression expression) implements Statement {

    @Override
    public ProgramState execute(ProgramState state) {
        SymbolTable sym = state.symbolTable();
        Heap heap = state.heap();

        if (!sym.isDefined(varName)) {
            throw new StatementExecutionException("wH: variable '" + varName + "' is not defined");
        }

        Value varValue = sym.getValue(varName);
        if (!(varValue instanceof RefValue refValue)) {
            throw new StatementExecutionException("wH: variable '" + varName + "' is not of reference type");
        }

        int address = refValue.getAddress();
        if (!heap.isDefined(address)) {
            throw new StatementExecutionException("wH: address " + address + " is not defined in heap");
        }

        Value eval = expression.evaluate(sym, heap);
        if (!eval.getType().equals(refValue.getLocationType())) {
            throw new StatementExecutionException("wH: type mismatch for variable '" + varName + "'");
        }

        heap.update(address, eval);
        return state;
    }

    @Override
    public String toString() {
        return "wH(" + varName + ", " + expression + ")";
    }
}
