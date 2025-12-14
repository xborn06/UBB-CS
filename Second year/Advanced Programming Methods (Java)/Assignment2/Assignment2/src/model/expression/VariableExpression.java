package model.expression;

import model.state.SymbolTable;
import model.value.Value;
import exceptions.ExpressionEvaluationException;

public record VariableExpression(String variableName) implements Expression {

    @Override
    public Value evaluate(SymbolTable symTable) {
        if(!symTable.isDefined(variableName)){
            throw new ExpressionEvaluationException("Variable '" + variableName + "' is not defined");
        }
        return symTable.getValue(variableName);
    }

    @Override
    public String toString() {
        return variableName;
    }
}