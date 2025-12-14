package model.statement;

import model.expression.Expression;
import model.state.ProgramState;
import model.value.BooleanValue;
import model.value.Value;
import exceptions.StatementExecutionException;

public record IfStatement(Expression condition, Statement thenBranch, Statement elseBranch) implements Statement {

    @Override
    public ProgramState execute(ProgramState state) {
        Value result = condition.evaluate(state.symbolTable(), state.heap());
        if (result instanceof BooleanValue booleanValue) {
            if (booleanValue.value()) {
                state.executionStack().push(thenBranch);
            } else {
                state.executionStack().push(elseBranch);
            }
        } else {
            throw new StatementExecutionException("Condition expression does not evaluate to a boolean");
        }
        return state;
    }

    @Override
    public String toString() {
        return "if (" + condition + ") then (" + thenBranch + ") else (" + elseBranch + ")";
    }
}
