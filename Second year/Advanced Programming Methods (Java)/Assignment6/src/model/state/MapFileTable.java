package model.state;

import model.value.StringValue;
import java.io.BufferedReader;
import java.util.HashMap;
import java.util.Map;

public class MapFileTable implements FileTable {
    private final Map<StringValue, BufferedReader> map = new HashMap<>();

    @Override public boolean contains(StringValue key) { return map.containsKey(key); }
    @Override public BufferedReader get(StringValue key) { return map.get(key); }
    @Override public void put(StringValue key, BufferedReader br) { map.put(key, br); }
    @Override public void remove(StringValue key) { map.remove(key); }
    @Override public String toString() { return map.keySet().toString(); }
}
