package controller;

import model.state.ProgramState;
import model.state.Heap;
import model.value.RefValue;
import model.value.Value;
import model.statement.Statement;
import repository.Repository;
import exceptions.MyException;

import java.util.*;
import java.util.stream.Collectors;

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

        repository.logProgramStateExecution();
        while (!currentState.executionStack().isEmpty()) {
            oneStep();
            currentState = repository.getCurrentProgram();

            Heap heap = currentState.heap();
            Map<Integer, Value> heapContent = heap.getContent();
            List<Integer> addresses = getReachableAddresses(
                    currentState.symbolTable().getContent().values(),
                    heapContent
            );
            heap.setContent(garbageCollector(addresses, heapContent));

            repository.logProgramStateExecution();
        }
    }

    private Map<Integer, Value> garbageCollector(List<Integer> addresses, Map<Integer, Value> heap) {
        return heap.entrySet().stream()
                .filter(e -> addresses.contains(e.getKey()))
                .collect(Collectors.toMap(Map.Entry::getKey, Map.Entry::getValue));
    }


    private List<Integer> getReachableAddresses(Collection<Value> symTableValues,
                                                Map<Integer, Value> heap) {
        Set<Integer> visited = new HashSet<>();
        Deque<Value> workList = new ArrayDeque<>(symTableValues);

        while (!workList.isEmpty()) {
            Value v = workList.pop();
            if (v instanceof RefValue ref) {
                int addr = ref.getAddress();
                if (addr != 0 && visited.add(addr)) {
                    Value pointed = heap.get(addr);
                    if (pointed != null) {
                        workList.add(pointed);
                    }
                }
            }
        }

        return new ArrayList<>(visited);
    }

}
