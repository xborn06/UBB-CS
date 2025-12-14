package model.statement;

import exceptions.MyException;
import exceptions.StatementExecutionException;
import model.adt.MyIDictionary;
import model.expression.Expression;
import model.state.ProgramState;
import model.type.StringType;
import model.type.Type;
import model.value.StringValue;
import model.value.Value;

import java.io.BufferedReader;
import java.io.FileReader;
import java.io.IOException;

public record OpenRFileStatement(Expression exp) implements Statement {
    @Override
    public ProgramState execute(ProgramState state) {
        Value v = exp.evaluate(state.symbolTable(), state.heap());
        if (!(v instanceof StringValue sv)) {
            throw new StatementExecutionException("openRFile: expression is not a string");
        }

        var ft = state.fileTable();
        if (ft.contains(sv)) {
            throw new StatementExecutionException("openRFile: file already opened: " + sv);
        }
        try {
            BufferedReader br = new BufferedReader(new FileReader(sv.get()));
            ft.put(sv, br);
            return null;
        } catch (IOException e) {
            throw new StatementExecutionException("openRFile: " + e.getMessage());
        }
    }

    @Override
    public MyIDictionary<String, Type> typecheck(MyIDictionary<String, Type> typeEnv) throws MyException {
        Type typexp = exp.typecheck(typeEnv);
        if (!typexp.equals(new StringType())) {
            throw new MyException("openRFile: expression is not a string");
        }
        return typeEnv;
    }

    @Override
    public String toString() {
        return "openRFile(" + exp + ")";
    }
}
