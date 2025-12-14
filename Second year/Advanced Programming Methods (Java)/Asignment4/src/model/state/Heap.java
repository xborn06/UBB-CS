package model.state;

import model.value.Value;

import java.util.Map;

public interface Heap {
    int allocate(Value value);
    Value get(int address);
    void update(int address, Value value);
    boolean isDefined(int address);

    Map<Integer, Value> getContent();
    void setContent(Map<Integer, Value> newContent);
}
