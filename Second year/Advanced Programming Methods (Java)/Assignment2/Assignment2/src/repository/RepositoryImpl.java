package repository;

import model.state.ProgramState;
import exceptions.MyException;

import java.util.ArrayList;
import java.util.List;

public class RepositoryImpl implements Repository {
    private List<ProgramState> programStates;
    private int currentIndex;

    public RepositoryImpl() {
        this.programStates = new ArrayList<>();
        this.currentIndex = 0;
    }

    @Override
    public ProgramState getCurrentProgram() {
        if (programStates.isEmpty()) {
            throw new MyException("No programs in repository");
        }
        return programStates.get(currentIndex);
    }

    @Override
    public void setCurrentProgram(ProgramState program) {
        if (programStates.isEmpty()) {
            programStates.add(program);
        } else {
            programStates.set(currentIndex, program);
        }
    }

    @Override
    public void addProgram(ProgramState program) {
        programStates.add(program);
    }

    @Override
    public void logProgramStateExecution() throws MyException {
        System.out.println("=== PROGRAM STATE ===");
        System.out.println(getCurrentProgram());
        System.out.println("=====================");
    }

    @Override
    public void clearPrograms() {
        programStates.clear();
        currentIndex = 0;
    }
}