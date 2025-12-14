package model.statement;

import exceptions.MyException;
import model.adt.MyIDictionary;
import exceptions.StatementExecutionException;
import model.expression.Expression;
import model.state.ProgramState;
import model.state.SymbolTable;
import model.type.Type;
import model.value.Value;

public record AssignmentStatement(Expression expression, String variableName) implements Statement {

    @Override
    public ProgramState execute(ProgramState state) {
        SymbolTable symbolTable = state.symbolTable();
        if (!symbolTable.isDefined(variableName)) {
            throw new StatementExecutionException("Variable '" + variableName + "' is not defined");
        }
        Value value = expression.evaluate(symbolTable, state.heap());
        if (!value.getType().equals(symbolTable.getType(variableName))) {
            throw new StatementExecutionException("Type mismatch for variable '" + variableName + "'");
        }
        symbolTable.update(variableName, value);
        return null;
    }

    @Override
    public MyIDictionary<String, Type> typecheck(MyIDictionary<String, Type> typeEnv) throws MyException {
        Type typevar = typeEnv.lookup(variableName);
        Type typexp = expression.typecheck(typeEnv);
        if (typevar.equals(typexp)) {
            return typeEnv;
        }
        throw new MyException("Assignment: right hand side and left hand side have different types");
    }

    @Override
    public String toString() {
        return variableName + " = " + expression;
    }
}
