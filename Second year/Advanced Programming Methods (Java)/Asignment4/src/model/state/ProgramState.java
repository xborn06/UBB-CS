package model.state;

import model.statement.Statement;

public class ProgramState {
    private final ExecutionStack executionStack;
    private final SymbolTable symbolTable;
    private final Out out;
    private final FileTable fileTable;
    private final Heap heap;
    private final Statement originalProgram;

    public ProgramState(ExecutionStack executionStack,
                        SymbolTable symbolTable,
                        Out out,
                        FileTable fileTable,
                        Heap heap,
                        Statement originalProgram) {
        this.executionStack = executionStack;
        this.symbolTable = symbolTable;
        this.out = out;
        this.fileTable = fileTable;
        this.heap = heap;
        this.originalProgram = originalProgram;

        this.executionStack.push(originalProgram);
    }

    public ProgramState(ExecutionStack executionStack,
                        SymbolTable symbolTable,
                        Out out,
                        FileTable fileTable,
                        Statement originalProgram) {
        this(executionStack, symbolTable, out, fileTable, new MapHeap(), originalProgram);
    }

    public ExecutionStack executionStack() {
        return executionStack;
    }

    public SymbolTable symbolTable() {
        return symbolTable;
    }

    public Out out() {
        return out;
    }

    public FileTable fileTable() {
        return fileTable;
    }

    public Heap heap() {
        return heap;
    }

    public Statement getOriginalProgram() {
        return originalProgram;
    }

    public boolean isCompleted() {
        return executionStack.isEmpty();
    }

    @Override
    public String toString() {
        StringBuilder sb = new StringBuilder();
        sb.append("\n=== Program State ===\n");

        sb.append("Execution Stack:\n");
        sb.append(executionStack).append("\n");

        sb.append("Symbol Table:\n");
        sb.append(symbolTable).append("\n");

        sb.append("Heap:\n");
        sb.append(heap).append("\n");

        sb.append("Output:\n");
        sb.append(out).append("\n");

        sb.append("File Table:\n");
        sb.append(fileTable).append("\n");

        sb.append("======================\n");
        return sb.toString();
    }
}
