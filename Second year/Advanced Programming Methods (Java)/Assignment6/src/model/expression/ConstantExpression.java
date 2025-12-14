package model.expression;

import exceptions.MyException;
import model.adt.MyIDictionary;
import model.state.Heap;
import model.state.SymbolTable;
import model.type.Type;
import model.value.Value;

public record ConstantExpression(Value value) implements Expression {

    @Override
    public Value evaluate(SymbolTable symTable, Heap heap) {
        return value;
    }

    @Override
    public Type typecheck(MyIDictionary<String, Type> typeEnv) throws MyException {
        return value.getType();
    }

    @Override
    public String toString() {
        return value.toString();
    }
}
