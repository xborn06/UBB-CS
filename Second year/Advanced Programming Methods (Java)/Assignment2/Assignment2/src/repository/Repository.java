package repository;

import model.state.ProgramState;
import exceptions.MyException;

public interface Repository {
    ProgramState getCurrentProgram();
    void setCurrentProgram(ProgramState program);
    void logProgramStateExecution() throws MyException;
    void addProgram(ProgramState program);
    void clearPrograms();
}