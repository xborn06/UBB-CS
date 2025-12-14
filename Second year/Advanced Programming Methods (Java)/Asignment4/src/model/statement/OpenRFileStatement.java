package model.statement;

import model.expression.Expression;
import model.state.ProgramState;
import model.value.StringValue;
import model.value.Value;
import exceptions.StatementExecutionException;

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
            return state;
        } catch (IOException e) {
            throw new StatementExecutionException("openRFile: " + e.getMessage());
        }
    }

    @Override
    public String toString() { return "openRFile(" + exp + ")"; }
}
