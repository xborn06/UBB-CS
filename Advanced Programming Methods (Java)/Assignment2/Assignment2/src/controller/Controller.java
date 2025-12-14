package controller;

import exceptions.MyException;

public interface Controller {
    void oneStep() throws MyException;
    void allSteps() throws MyException;
    void setDisplayFlag(boolean displayFlag);
    void addProgram(model.state.ProgramState program);
}