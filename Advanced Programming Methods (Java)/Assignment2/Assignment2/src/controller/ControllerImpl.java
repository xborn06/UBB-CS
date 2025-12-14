package controller;

import model.state.ProgramState;
import model.statement.Statement;
import repository.Repository;
import exceptions.MyException;

public class ControllerImpl implements Controller {
    private Repository repository;
    private boolean displayFlag;

    public ControllerImpl(Repository repository) {
        this.repository = repository;
        this.displayFlag = false;
    }

    public ControllerImpl(Repository repository, boolean displayFlag) {
        this.repository = repository;
        this.displayFlag = displayFlag;
    }

    @Override
    public void oneStep() throws MyException {
        ProgramState currentState = repository.getCurrentProgram();
        var executionStack = currentState.executionStack();

        if (executionStack.isEmpty()) {
            throw new MyException("Execution stack is empty");
        }

        Statement currentStatement = executionStack.pop();
        if (displayFlag) {
            System.out.println(">>> Executing: " + currentStatement);
        }

        currentStatement.execute(currentState);
        repository.setCurrentProgram(currentState);

        if (displayFlag) {
            repository.logProgramStateExecution();
        }
    }

    @Override
    public void allSteps() throws MyException {
        ProgramState currentState = repository.getCurrentProgram();

        if (displayFlag) {
            repository.logProgramStateExecution();
        }

        while (!currentState.executionStack().isEmpty()) {
            oneStep();
        }

        if (displayFlag) {
            System.out.println(">>> Program execution completed!");
            System.out.println("Final output: " + currentState.out());
        }
    }

    @Override
    public void setDisplayFlag(boolean displayFlag) {
        this.displayFlag = displayFlag;
    }

    @Override
    public void addProgram(ProgramState program) {
        repository.addProgram(program);
    }
}