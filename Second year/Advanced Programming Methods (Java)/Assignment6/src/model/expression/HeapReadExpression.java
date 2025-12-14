package model.expression;

import exceptions.MyException;
import model.adt.MyIDictionary;
import model.state.Heap;
import model.state.SymbolTable;
import model.type.RefType;
import model.type.Type;
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
    public Type typecheck(MyIDictionary<String, Type> typeEnv) throws MyException {
        Type typ = expression.typecheck(typeEnv);
        if (typ instanceof RefType refType) {
            return refType.getInner();
        }
        throw new MyException("the rH argument is not a Ref Type");
    }

    @Override
    public String toString() {
        return "rH(" + expression + ")";
    }
}
