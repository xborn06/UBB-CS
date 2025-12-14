package repository;

import model.state.ProgramState;
import exceptions.MyException;

import java.io.BufferedWriter;
import java.io.FileWriter;
import java.io.IOException;
import java.io.PrintWriter;
import java.util.ArrayList;
import java.util.List;

public class RepositoryImpl implements Repository {
    private final List<ProgramState> programStates;
    private int currentIndex;
    private final String logFilePath;

    public RepositoryImpl(String logFilePath) {
        this.programStates = new ArrayList<>();
        this.currentIndex = 0;
        this.logFilePath = logFilePath;
    }

    public RepositoryImpl() {
        this("log.txt");
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
        try (PrintWriter pw = new PrintWriter(new BufferedWriter(new FileWriter(logFilePath, true)))) {
            ProgramState prg = getCurrentProgram();

            pw.println("ExeStack:");
            pw.println(prg.executionStack());

            pw.println("SymTable:");
            pw.println(prg.symbolTable());

            pw.println("Out:");
            pw.println(prg.out());



            pw.println("-----------------------------");
        } catch (IOException e) {
            throw new MyException("Error writing log: " + e.getMessage());
        }
    }

    @Override
    public void clearPrograms() {
        programStates.clear();
        currentIndex = 0;
    }
}
