package model.statement;

import exceptions.MyException;
import model.adt.MyIDictionary;
import exceptions.StatementExecutionException;
import model.expression.Expression;
import model.state.ProgramState;
import model.type.BoolType;
import model.type.Type;
import model.value.BooleanValue;
import model.value.Value;

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

        return null;
    }

    @Override
    public MyIDictionary<String, Type> typecheck(MyIDictionary<String, Type> typeEnv) throws MyException {
        Type typexp = condition.typecheck(typeEnv);
        if (!typexp.equals(new BoolType())) {
            throw new MyException("The condition of WHILE has not the type bool");
        }
        body.typecheck(typeEnv.deepCopy());
        return typeEnv;
    }

    @Override
    public String toString() {
        return "while (" + condition + ") " + body;
    }
}
