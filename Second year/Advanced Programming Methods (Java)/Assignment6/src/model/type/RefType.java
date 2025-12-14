package model.type;

import model.value.RefValue;
import model.value.Value;

public class RefType implements Type {
    private final Type inner;

    public RefType(Type inner) {
        this.inner = inner;
    }

    public Type getInner() {
        return inner;
    }

    @Override
    public Value getDefaultValue() {
        return new RefValue(0, inner);
    }

    @Override
    public boolean equals(Object another) {
        if (this == another) return true;
        if (!(another instanceof RefType other)) return false;
        return inner.equals(other.inner);
    }

    @Override
    public int hashCode() {
        return 31 * inner.hashCode() + 7;
    }

    @Override
    public String toString() {
        return "Ref(" + inner + ")";
    }
}
