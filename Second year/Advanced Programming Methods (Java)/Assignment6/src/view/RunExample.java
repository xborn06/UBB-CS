package view;

import controller.ControllerImpl;
import exceptions.MyException;

public class RunExample extends Command {
    private final ControllerImpl controller;

    public RunExample(String key, String description, ControllerImpl controller) {
        super(key, description);
        this.controller = controller;
    }

    @Override
    public void execute() {
        try {
            controller.allSteps();
        } catch (MyException e) {
            System.out.println("Error: " + e.getMessage());
        }
    }
}
