package model.expression;

import model.state.Heap;
import model.state.SymbolTable;
import model.value.Value;

public interface Expression {
    Value evaluate(SymbolTable symTable, Heap heap);
}
