package model.state;

import exceptions.MyException;
import model.statement.Statement;

public class ProgramState {
    private static int lastId = 0;

    private static synchronized int getNextId() {
        return ++lastId;
    }

    private final ExecutionStack executionStack;
    private final SymbolTable symbolTable;
    private final Out out;
    private final FileTable fileTable;
    private final Heap heap;
    private final Statement originalProgram;
    private final int id;

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

        this.id = getNextId();
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

    public int getId() {
        return id;
    }

    public boolean isCompleted() {
        return executionStack.isEmpty();
    }

    public boolean isNotCompleted() {
        return !executionStack.isEmpty();
    }

    public ProgramState oneStep() throws MyException {
        if (executionStack.isEmpty()) {
            throw new MyException("program state stack is empty");
        }
        Statement currentStatement = executionStack.pop();
        return currentStatement.execute(this);
    }

    @Override
    public String toString() {
        StringBuilder sb = new StringBuilder();
        sb.append("\n=== Program State ").append(id).append(" ===\n");

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
