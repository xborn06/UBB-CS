package model.state;

import model.value.StringValue;
import java.io.BufferedReader;

public interface FileTable {
    boolean contains(StringValue key);
    BufferedReader get(StringValue key);
    void put(StringValue key, BufferedReader br);
    void remove(StringValue key);
    String toString();
}
