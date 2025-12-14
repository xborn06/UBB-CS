package controller;

import exceptions.MyException;

public interface Controller {
    void oneStep() throws MyException;
    void allSteps() throws MyException;
}