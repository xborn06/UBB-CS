package model.state;

import model.statement.Statement;
import exceptions.ADTException;

import java.util.Deque;
import java.util.LinkedList;

public class StackExecutionStack implements ExecutionStack {
    private final Deque<Statement> stack = new LinkedList<>();

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