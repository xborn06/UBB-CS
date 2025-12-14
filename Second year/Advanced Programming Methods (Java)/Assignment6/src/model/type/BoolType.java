package model.type;

import model.value.BooleanValue;
import model.value.Value;

public class BoolType implements Type {
    @Override
    public Value getDefaultValue() {
        return new BooleanValue(false);
    }

    @Override
    public boolean equals(Object another) {
        return another instanceof BoolType;
    }

    @Override
    public int hashCode() {
        return 2;
    }

    @Override
    public String toString() {
        return "bool";
    }
}
