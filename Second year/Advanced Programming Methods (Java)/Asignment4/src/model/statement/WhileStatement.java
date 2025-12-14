package model.statement;

import model.expression.Expression;
import model.state.ProgramState;
import model.value.BooleanValue;
import model.value.Value;
import exceptions.StatementExecutionException;

public record WhileStatement(Expression condition, Statement body) implements Statement {

    @Override
    public ProgramState execute(ProgramState state) {
        Value v = condition.evaluate(state.symbolTable(), state.heap());
        if (!(v instanceof BooleanValue b)) {
            throw new StatementExecutionException("while: condition is not a boolean");
        }

        if (b.value()) {
            var stack = state.executionStack();
            stack.push(this);
            stack.push(body);
        }

        return state;
    }

    @Override
    public String toString() {
        return "while (" + condition + ") " + body;
    }
}
