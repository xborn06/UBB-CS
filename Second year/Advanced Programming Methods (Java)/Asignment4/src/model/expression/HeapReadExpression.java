package model.expression;

import model.state.Heap;
import model.state.SymbolTable;
import model.value.RefValue;
import model.value.Value;
import exceptions.ExpressionEvaluationException;

public record HeapReadExpression(Expression expression) implements Expression {

    @Override
    public Value evaluate(SymbolTable symTable, Heap heap) {
        Value v = expression.evaluate(symTable, heap);
        if (!(v instanceof RefValue ref)) {
            throw new ExpressionEvaluationException("rH argument is not a RefValue");
        }
        int addr = ref.getAddress();
        if (!heap.isDefined(addr)) {
            throw new ExpressionEvaluationException("Address " + addr + " is not defined in heap");
        }
        return heap.get(addr);
    }

    @Override
    public String toString() {
        return "rH(" + expression + ")";
    }
}
