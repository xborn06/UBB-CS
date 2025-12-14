package model.state;

import model.value.Value;
import java.util.ArrayList;
import java.util.List;

public class ListOut implements Out {
    private final List<Value> outputList;

    public ListOut() {
        outputList = new ArrayList<>();
    }

    @Override
    public void add(Value value) {
        outputList.add(value);
    }

    @Override
    public String toString() {
        return outputList.toString();
    }
}