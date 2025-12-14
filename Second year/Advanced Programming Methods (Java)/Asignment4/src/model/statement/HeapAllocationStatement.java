package model.statement;

import model.expression.Expression;
import model.state.Heap;
import model.state.ProgramState;
import model.state.SymbolTable;
import model.type.Type;
import model.value.RefValue;
import model.value.Value;
import exceptions.StatementExecutionException;

public record HeapAllocationStatement(String varName, Expression expression) implements Statement {

    @Override
    public ProgramState execute(ProgramState state) {
        SymbolTable sym = state.symbolTable();
        Heap heap = state.heap();

        if (!sym.isDefined(varName)) {
            throw new StatementExecutionException("new: variable '" + varName + "' is not defined");
        }

        Value varValue = sym.getValue(varName);
        if (!(varValue instanceof RefValue refValue)) {
            throw new StatementExecutionException("new: variable '" + varName + "' is not of reference type");
        }

        Value eval = expression.evaluate(sym, heap);
        Type locationType = refValue.getLocationType();

        if (!eval.getType().equals(locationType)) {
            throw new StatementExecutionException("new: type mismatch for variable '" + varName + "'");
        }

        int address = heap.allocate(eval);
        sym.update(varName, new RefValue(address, locationType));

        return state;
    }

    @Override
    public String toString() {
        return "new(" + varName + ", " + expression + ")";
    }
}
