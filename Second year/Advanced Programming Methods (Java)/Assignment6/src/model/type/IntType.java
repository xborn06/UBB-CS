package model.type;

import model.value.IntegerValue;
import model.value.Value;

public class IntType implements Type {
    @Override
    public Value getDefaultValue() {
        return new IntegerValue(0);
    }

    @Override
    public boolean equals(Object another) {
        return another instanceof IntType;
    }

    @Override
    public int hashCode() {
        return 1;
    }

    @Override
    public String toString() {
        return "int";
    }
}
