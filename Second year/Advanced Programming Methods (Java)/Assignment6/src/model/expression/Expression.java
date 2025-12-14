package model.expression;

import exceptions.MyException;
import model.adt.MyIDictionary;
import model.state.Heap;
import model.state.SymbolTable;
import model.type.Type;
import model.value.Value;

public interface Expression {
    Value evaluate(SymbolTable symTable, Heap heap);

    Type typecheck(MyIDictionary<String, Type> typeEnv) throws MyException;
}
