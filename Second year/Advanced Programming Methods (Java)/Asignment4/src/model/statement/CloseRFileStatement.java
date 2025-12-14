package model.statement;

import model.expression.Expression;
import model.state.ProgramState;
import model.value.StringValue;
import model.value.Value;
import exceptions.StatementExecutionException;

import java.io.BufferedReader;
import java.io.IOException;

public record CloseRFileStatement(Expression exp) implements Statement {
    @Override
    public ProgramState execute(ProgramState state) {
        Value v = exp.evaluate(state.symbolTable(), state.heap());
        if (!(v instanceof StringValue sv)) {
            throw new StatementExecutionException("closeRFile: expression is not a string");
        }

        var ft = state.fileTable();
        if (!ft.contains(sv)) {
            throw new StatementExecutionException("closeRFile: file is not opened: " + sv);
        }
        BufferedReader br = ft.get(sv);
        try {
            br.close();
        } catch (IOException e) {
            throw new StatementExecutionException("closeRFile: " + e.getMessage());
        }
        ft.remove(sv);
        return state;
    }

    @Override
    public String toString() { return "closeRFile(" + exp + ")"; }
}
