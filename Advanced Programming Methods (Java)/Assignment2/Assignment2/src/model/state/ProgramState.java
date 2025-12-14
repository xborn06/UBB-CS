package model.state;

public record ProgramState(ExecutionStack executionStack, SymbolTable symbolTable, Out out) {

    public ProgramState {
    }

    public boolean isCompleted() {
        return executionStack.isEmpty();
    }

    @Override
    public String toString() {
        return "ExecutionStack:\n" + executionStack + "\n\n" +
                "SymbolTable:\n" + symbolTable + "\n\n" +
                "Out:\n" + out + "\n";
    }
}