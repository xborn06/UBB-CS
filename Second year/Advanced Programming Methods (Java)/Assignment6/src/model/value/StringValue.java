package model.value;

import model.type.StringType;
import model.type.Type;

public final class StringValue implements Value {
    private final String value;

    public StringValue(String value) { this.value = value; }

    public String get() { return value; }

    @Override
    public Type getType() { return new StringType(); }

    @Override
    public String toString() { return value; }

    @Override
    public boolean equals(Object o) {
        if (this == o) return true;
        if (!(o instanceof StringValue sv)) return false;
        return value.equals(sv.value);
    }

    @Override
    public int hashCode() { return value.hashCode(); }
}
