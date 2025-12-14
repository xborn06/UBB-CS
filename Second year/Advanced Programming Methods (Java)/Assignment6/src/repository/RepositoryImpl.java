package repository;

import exceptions.MyException;
import model.state.ProgramState;

import java.io.BufferedWriter;
import java.io.FileWriter;
import java.io.IOException;
import java.io.PrintWriter;
import java.util.ArrayList;
import java.util.List;

public class RepositoryImpl implements Repository {
    private final List<ProgramState> programStates;
    private final String logFilePath;

    public RepositoryImpl(String logFilePath) {
        this.programStates = new ArrayList<>();
        this.logFilePath = logFilePath;
    }

    @Override
    public List<ProgramState> getPrgList() {
        return programStates;
    }

    @Override
    public void setPrgList(List<ProgramState> programs) {
        programStates.clear();
        programStates.addAll(programs);
    }

    @Override
    public void addProgram(ProgramState program) {
        programStates.add(program);
    }

    @Override
    public void logPrgStateExec(ProgramState prg) throws MyException {
        try (PrintWriter pw = new PrintWriter(new BufferedWriter(new FileWriter(logFilePath, true)))) {
            pw.println(prg.toString());
        } catch (IOException e) {
            throw new MyException("Error writing log: " + e.getMessage());
        }
    }

    @Override
    public void clearPrograms() {
        programStates.clear();
    }
}
