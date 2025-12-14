package model.adt;

import exceptions.MyException;

import java.util.HashMap;
import java.util.Map;

public class MyDictionary<K, V> implements MyIDictionary<K, V> {
    private final Map<K, V> map;

    public MyDictionary() {
        this.map = new HashMap<>();
    }

    private MyDictionary(Map<K, V> backing) {
        this.map = backing;
    }

    @Override
    public void add(K key, V value) {
        map.put(key, value);
    }

    @Override
    public boolean isDefined(K key) {
        return map.containsKey(key);
    }

    @Override
    public V lookup(K key) throws MyException {
        if (!map.containsKey(key)) {
            throw new MyException("Undefined key: " + key);
        }
        return map.get(key);
    }

    @Override
    public MyIDictionary<K, V> deepCopy() {
        return new MyDictionary<>(new HashMap<>(map));
    }

    @Override
    public Map<K, V> getContent() {
        return map;
    }

    @Override
    public String toString() {
        return map.toString();
    }
}
