package repository;

import exceptions.MyException;
import model.state.ProgramState;

import java.util.List;

public interface Repository {
    List<ProgramState> getPrgList();
    void setPrgList(List<ProgramState> programs);

    void logPrgStateExec(ProgramState program) throws MyException;

    void addProgram(ProgramState program);
    void clearPrograms();
}
