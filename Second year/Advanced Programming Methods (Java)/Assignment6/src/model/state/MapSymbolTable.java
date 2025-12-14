package model.state;

import model.type.Type;
import model.value.Value;
import exceptions.StatementExecutionException;
import exceptions.ExpressionEvaluationException;

import java.util.HashMap;
import java.util.Map;

public class MapSymbolTable implements SymbolTable {
    private final Map<String, Value> map = new HashMap<>();

    @Override
    public boolean isDefined(String variableName) {
        return map.containsKey(variableName);
    }

    @Override
    public Type getType(String variableName) {
        if (!isDefined(variableName)) {
            throw new ExpressionEvaluationException("Variable '" + variableName + "' is not defined");
        }
        return map.get(variableName).getType();
    }

    @Override
    public void declareVariable(String variableName, Type type) {
        if (isDefined(variableName)) {
            throw new StatementExecutionException("Variable '" + variableName + "' is already declared");
        }
        map.put(variableName, type.getDefaultValue());
    }

    @Override
    public void update(String variableName, Value value) {
        if (!isDefined(variableName)) {
            throw new StatementExecutionException("Variable '" + variableName + "' is not defined");
        }
        map.put(variableName, value);
    }

    @Override
    public Value getValue(String variableName) {
        if (!isDefined(variableName)) {
            throw new ExpressionEvaluationException("Variable '" + variableName + "' is not defined");
        }
        return map.get(variableName);
    }

    @Override
    public Map<String, Value> getContent() {
        return map;
    }

    @Override
    public String toString() {
        return map.toString();
    }
}
