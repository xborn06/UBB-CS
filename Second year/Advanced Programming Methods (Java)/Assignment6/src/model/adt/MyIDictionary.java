package model.adt;

import exceptions.MyException;

import java.util.Map;

public interface MyIDictionary<K, V> {
    void add(K key, V value);

    boolean isDefined(K key);

    V lookup(K key) throws MyException;

    MyIDictionary<K, V> deepCopy();

    Map<K, V> getContent();
}
