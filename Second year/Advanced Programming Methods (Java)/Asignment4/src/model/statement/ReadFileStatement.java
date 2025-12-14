package model.statement;

import model.expression.Expression;
import model.state.ProgramState;
import model.type.IntType;
import model.value.IntegerValue;
import model.value.StringValue;
import model.value.Value;
import exceptions.StatementExecutionException;

import java.io.BufferedReader;
import java.io.IOException;

public record ReadFileStatement(Expression exp, String varName) implements Statement {
    @Override
    public ProgramState execute(ProgramState state) {
        var sym = state.symbolTable();
        if (!sym.isDefined(varName) || !(sym.getType(varName) instanceof IntType)) {
            throw new StatementExecutionException("readFile: '" + varName + "' must be an int variable");
        }

        Value v = exp.evaluate(sym, state.heap());
        if (!(v instanceof StringValue sv)) {
            throw new StatementExecutionException("readFile: expression is not a string");
        }

        var ft = state.fileTable();
        if (!ft.contains(sv)) {
            throw new StatementExecutionException("readFile: file not opened: " + sv);
        }

        BufferedReader br = ft.get(sv);
        try {
            String line = br.readLine();
            int val = (line == null || line.isEmpty()) ? 0 : Integer.parseInt(line.trim());
            sym.update(varName, new IntegerValue(val));
            return state;
        } catch (IOException | NumberFormatException e) {
            throw new StatementExecutionException("readFile: " + e.getMessage());
        }
    }

    @Override
    public String toString() { return "readFile(" + exp + ", " + varName + ")"; }
}
