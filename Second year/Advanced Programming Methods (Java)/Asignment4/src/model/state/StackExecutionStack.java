package model.state;

import model.statement.Statement;
import exceptions.ADTException;

import java.util.LinkedList;
import java.util.List;

public class StackExecutionStack implements ExecutionStack {
    private final List<Statement> stack = new LinkedList<>();

    @Override
    public void push(Statement statement) {
        stack.addFirst(statement);
    }

    @Override
    public Statement pop() {
        if (stack.isEmpty()) {
            throw new ADTException("Cannot pop from empty execution stack");
        }
        return stack.removeFirst();
    }

    @Override
    public boolean isEmpty() {
        return stack.isEmpty();
    }

    @Override
    public String toString() {
        return stack.toString();
    }
}