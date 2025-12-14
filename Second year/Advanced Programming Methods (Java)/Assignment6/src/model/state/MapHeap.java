package model.state;

import model.value.Value;
import exceptions.ExpressionEvaluationException;

import java.util.HashMap;
import java.util.Map;

public class MapHeap implements Heap {
    private final Map<Integer, Value> heap = new HashMap<>();
    private int nextFreeAddress = 1;

    private int getNextFreeAddress() {
        while (heap.containsKey(nextFreeAddress)) {
            nextFreeAddress++;
        }
        return nextFreeAddress;
    }

    @Override
    public int allocate(Value value) {
        int address = getNextFreeAddress();
        heap.put(address, value);
        return address;
    }

    @Override
    public Value get(int address) {
        if (!heap.containsKey(address)) {
            throw new ExpressionEvaluationException("Invalid heap address: " + address);
        }
        return heap.get(address);
    }

    @Override
    public void update(int address, Value value) {
        if (!heap.containsKey(address)) {
            throw new ExpressionEvaluationException("Invalid heap address: " + address);
        }
        heap.put(address, value);
    }

    @Override
    public boolean isDefined(int address) {
        return heap.containsKey(address);
    }

    @Override
    public Map<Integer, Value> getContent() {
        return heap;
    }

    @Override
    public void setContent(Map<Integer, Value> newContent) {
        heap.clear();
        heap.putAll(newContent);
    }

    @Override
    public String toString() {
        return heap.toString();
    }
}
