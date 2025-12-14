package model.statement;

import exceptions.MyException;
import model.adt.MyIDictionary;
import model.state.*;
import model.type.Type;
import model.value.Value;

import java.util.Map;

public record ForkStatement(Statement statement) implements Statement {

    @Override
    public ProgramState execute(ProgramState state) {
        SymbolTable parentSymTable = state.symbolTable();
        Heap heap = state.heap();
        FileTable fileTable = state.fileTable();
        Out out = state.out();

        SymbolTable newSymTable = new MapSymbolTable();
        for (Map.Entry<String, Value> entry : parentSymTable.getContent().entrySet()) {
            String varName = entry.getKey();
            Value value = entry.getValue();
            newSymTable.declareVariable(varName, value.getType());
            newSymTable.update(varName, value);
        }

        ExecutionStack newStack = new StackExecutionStack();

        return new ProgramState(
                newStack,
                newSymTable,
                out,
                fileTable,
                heap,
                statement
        );
    }

    @Override
    public MyIDictionary<String, Type> typecheck(MyIDictionary<String, Type> typeEnv) throws MyException {
        statement.typecheck(typeEnv.deepCopy());
        return typeEnv;
    }

    @Override
    public String toString() {
        return "fork(" + statement + ")";
    }
}
