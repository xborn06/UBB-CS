package model.statement;

import exceptions.MyException;
import exceptions.StatementExecutionException;
import model.adt.MyIDictionary;
import model.expression.Expression;
import model.state.ProgramState;
import model.type.IntType;
import model.type.StringType;
import model.type.Type;
import model.value.IntegerValue;
import model.value.StringValue;
import model.value.Value;

import java.io.BufferedReader;
import java.io.IOException;

public record ReadFileStatement(Expression exp, String varName) implements Statement {
    @Override
    public ProgramState execute(ProgramState state) {
        var sym = state.symbolTable();
        if (!sym.isDefined(varName)) {
            throw new StatementExecutionException("readFile: variable '" + varName + "' is not defined");
        }

        if (!sym.getType(varName).equals(new IntType())) {
            throw new StatementExecutionException("readFile: variable '" + varName + "' is not int");
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
            return null;
        } catch (IOException | NumberFormatException e) {
            throw new StatementExecutionException("readFile: " + e.getMessage());
        }
    }

    @Override
    public MyIDictionary<String, Type> typecheck(MyIDictionary<String, Type> typeEnv) throws MyException {
        Type typevar = typeEnv.lookup(varName);
        if (!typevar.equals(new IntType())) {
            throw new MyException("readFile: variable is not int");
        }

        Type typexp = exp.typecheck(typeEnv);
        if (!typexp.equals(new StringType())) {
            throw new MyException("readFile: expression is not a string");
        }

        return typeEnv;
    }

    @Override
    public String toString() {
        return "readFile(" + exp + ", " + varName + ")";
    }
}
