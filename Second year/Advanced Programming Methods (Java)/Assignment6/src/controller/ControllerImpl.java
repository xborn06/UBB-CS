package controller;

import exceptions.MyException;
import model.state.Heap;
import model.state.ProgramState;
import model.value.RefValue;
import model.value.Value;
import repository.Repository;

import java.util.*;
import java.util.concurrent.*;
import java.util.stream.Collectors;

public class ControllerImpl implements Controller {
    private final Repository repository;
    private final boolean displayFlag;
    private ExecutorService executor;

    public ControllerImpl(Repository repository) {
        this(repository, false);
    }

    public ControllerImpl(Repository repository, boolean displayFlag) {
        this.repository = repository;
        this.displayFlag = displayFlag;
    }

    private List<ProgramState> removeCompletedPrg(List<ProgramState> inPrgList) {
        return inPrgList.stream()
                .filter(ProgramState::isNotCompleted)
                .collect(Collectors.toList());
    }

    private void oneStepForAllPrg(List<ProgramState> prgList) throws MyException {
        for (ProgramState prg : prgList) {
            repository.logPrgStateExec(prg);
        }

        List<Callable<ProgramState>> callList = prgList.stream()
                .map((ProgramState p) -> (Callable<ProgramState>) () -> {
                    if (displayFlag && !p.executionStack().isEmpty()) {
                        System.out.println(">>> [Program " + p.getId() + "] executing one step");
                    }
                    return p.oneStep();
                })
                .collect(Collectors.toList());

        List<ProgramState> newPrgList;
        try {
            newPrgList = executor.invokeAll(callList).stream()
                    .map(future -> {
                        try {
                            return future.get();
                        } catch (InterruptedException e) {
                            Thread.currentThread().interrupt();
                            return null;
                        } catch (ExecutionException e) {
                            throw new RuntimeException(e.getCause());
                        }
                    })
                    .filter(Objects::nonNull)
                    .collect(Collectors.toList());
        } catch (InterruptedException e) {
            Thread.currentThread().interrupt();
            throw new MyException("Execution interrupted: " + e.getMessage());
        }

        prgList.addAll(newPrgList);

        for (ProgramState prg : prgList) {
            repository.logPrgStateExec(prg);
        }

        repository.setPrgList(prgList);
    }

    private void performGarbageCollection(List<ProgramState> prgList) {
        if (prgList.isEmpty()) {
            return;
        }

        Heap heap = prgList.get(0).heap(); // shared heap
        Map<Integer, Value> heapContent = heap.getContent();

        Collection<Value> symTableValues = prgList.stream()
                .flatMap(p -> p.symbolTable().getContent().values().stream())
                .collect(Collectors.toList());

        List<Integer> addresses = getReachableAddresses(symTableValues, heapContent);
        heap.setContent(garbageCollector(addresses, heapContent));
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

    @Override
    public void allSteps() throws MyException {
        executor = Executors.newFixedThreadPool(2);

        List<ProgramState> prgList = removeCompletedPrg(repository.getPrgList());

        while (!prgList.isEmpty()) {
            performGarbageCollection(prgList);

            oneStepForAllPrg(prgList);

            prgList = removeCompletedPrg(repository.getPrgList());
        }

        executor.shutdownNow();

        repository.setPrgList(prgList);
    }
}
