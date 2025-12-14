package view;

import controller.Controller;
import controller.ControllerImpl;
import model.state.ProgramState;
import model.statement.Statement;
import repository.Repository;
import repository.RepositoryImpl;
import exceptions.MyException;

import java.util.Scanner;

public class TextView {
    private Controller controller;
    private Scanner scanner;

    public TextView(Controller controller) {
        this.controller = controller;
        this.scanner = new Scanner(System.in);
    }

    public void run() {
        System.out.println("=== Toy Language Interpreter ===");

        while (true) {
            printMenu();
            String choice = scanner.nextLine().trim();

            try {
                switch (choice) {
                    case "1":
                        runExample1();
                        break;
                    case "2":
                        runExample2();
                        break;
                    case "3":
                        runExample3();
                        break;
                    case "4":
                        runStepByStep();
                        break;
                    case "5":
                        runWithDisplay();
                        break;
                    case "0":
                        System.out.println("Goodbye!");
                        return;
                    default:
                        System.out.println("Invalid choice!");
                }
            } catch (MyException e) {
                System.out.println("Error: " + e.getMessage());
            } catch (Exception e) {
                System.out.println("Unexpected error: " + e.getMessage());
            }
        }
    }

    private void printMenu() {
        System.out.println("\n--- Menu ---");
        System.out.println("1. Run Example 1 (int v; v=2; Print(v))");
        System.out.println("2. Run Example 2 (int a; a=2+3*5; int b; b=a-4/2+7; Print(b))");
        System.out.println("3. Run Example 3 (bool a; a=false; int v; If a Then v=2 Else v=3; Print(v))");
        System.out.println("4. Run Step by Step");
        System.out.println("5. Run with Display");
        System.out.println("0. Exit");
        System.out.print("Choose an option: ");
    }

    private void runExample1() throws MyException {
        System.out.println("\n>>> Running Example 1...");

        Statement ex1 = createExample1();
        ProgramState state = createProgramState(ex1);


        Repository freshRepo = new RepositoryImpl();
        freshRepo.addProgram(state);
        Controller freshController = new ControllerImpl(freshRepo, true);

        freshController.allSteps();
    }

    private void runExample2() throws MyException {
        System.out.println("\n>>> Running Example 2...");

        Statement ex2 = createExample2();
        ProgramState state = createProgramState(ex2);


        Repository freshRepo = new RepositoryImpl();
        freshRepo.addProgram(state);
        Controller freshController = new ControllerImpl(freshRepo, true);

        freshController.allSteps();
    }

    private void runExample3() throws MyException {
        System.out.println("\n>>> Running Example 3...");

        Statement ex3 = createExample3();
        ProgramState state = createProgramState(ex3);

        Repository freshRepo = new RepositoryImpl();
        freshRepo.addProgram(state);
        Controller freshController = new ControllerImpl(freshRepo, true);

        freshController.allSteps();
    }

    private void runStepByStep() throws MyException {
        System.out.println("\n>>> Running Step by Step...");
        System.out.println("Select example (1, 2, or 3): ");
        String example = scanner.nextLine().trim();

        Statement stmt;
        switch (example) {
            case "1": stmt = createExample1(); break;
            case "2": stmt = createExample2(); break;
            case "3": stmt = createExample3(); break;
            default:
                System.out.println("Invalid example!");
                return;
        }

        ProgramState state = createProgramState(stmt);
        controller.addProgram(state);
        controller.setDisplayFlag(false);

        System.out.println("Press Enter to execute next step, or 'q' to quit...");

        while (!state.isCompleted()) {
            scanner.nextLine();
            if (scanner.hasNextLine() && scanner.nextLine().equalsIgnoreCase("q")) {
                break;
            }

            controller.oneStep();
            System.out.println(state);
        }

        if (state.isCompleted()) {
            System.out.println(">>> Program completed!");
            System.out.println("Final output: " + state.out());
        }
    }

    private void runWithDisplay() throws MyException {
        System.out.println("\n>>> Running with Display...");
        System.out.println("Select example (1, 2, or 3): ");
        String example = scanner.nextLine().trim();

        Statement stmt;
        switch (example) {
            case "1": stmt = createExample1(); break;
            case "2": stmt = createExample2(); break;
            case "3": stmt = createExample3(); break;
            default:
                System.out.println("Invalid example!");
                return;
        }


        ProgramState freshState = createProgramState(stmt);
        Repository freshRepo = new RepositoryImpl();
        freshRepo.addProgram(freshState);
        Controller freshController = new ControllerImpl(freshRepo, true);

        freshController.allSteps();
    }

    private ProgramState createProgramState(Statement statement) {
        ProgramState state = new ProgramState(
                new model.state.StackExecutionStack(),
                new model.state.MapSymbolTable(),
                new model.state.ListOut()
        );

        state.executionStack().push(statement);
        return state;
    }

    private Statement createExample1() {

        return new model.statement.CompoundStatement(
                new model.statement.VariableDeclarationStatement(model.type.Type.INTEGER, "v"),
                new model.statement.CompoundStatement(
                        new model.statement.AssignmentStatement(
                                new model.expression.ConstantExpression(new model.value.IntegerValue(2)),
                                "v"
                        ),
                        new model.statement.PrintStatement(
                                new model.expression.VariableExpression("v")
                        )
                )
        );
    }

    private Statement createExample2() {

        return new model.statement.CompoundStatement(
                new model.statement.VariableDeclarationStatement(model.type.Type.INTEGER, "a"),
                new model.statement.CompoundStatement(
                        new model.statement.AssignmentStatement(
                                new model.expression.BinaryOperatorExpression(
                                        "+",
                                        new model.expression.ConstantExpression(new model.value.IntegerValue(2)),
                                        new model.expression.BinaryOperatorExpression(
                                                "*",
                                                new model.expression.ConstantExpression(new model.value.IntegerValue(3)),
                                                new model.expression.ConstantExpression(new model.value.IntegerValue(5))
                                        )
                                ),
                                "a"
                        ),
                        new model.statement.CompoundStatement(
                                new model.statement.VariableDeclarationStatement(model.type.Type.INTEGER, "b"),
                                new model.statement.CompoundStatement(
                                        new model.statement.AssignmentStatement(
                                                new model.expression.BinaryOperatorExpression(
                                                        "+",
                                                        new model.expression.BinaryOperatorExpression(
                                                                "-",
                                                                new model.expression.VariableExpression("a"),
                                                                new model.expression.BinaryOperatorExpression(
                                                                        "/",
                                                                        new model.expression.ConstantExpression(new model.value.IntegerValue(4)),
                                                                        new model.expression.ConstantExpression(new model.value.IntegerValue(2))
                                                                )
                                                        ),
                                                        new model.expression.ConstantExpression(new model.value.IntegerValue(7))
                                                ),
                                                "b"
                                        ),
                                        new model.statement.PrintStatement(
                                                new model.expression.VariableExpression("b")
                                        )
                                )
                        )
                )
        );
    }

    private Statement createExample3() {

        return new model.statement.CompoundStatement(
                new model.statement.VariableDeclarationStatement(model.type.Type.BOOLEAN, "a"),
                new model.statement.CompoundStatement(
                        new model.statement.AssignmentStatement(
                                new model.expression.ConstantExpression(new model.value.BooleanValue(false)),
                                "a"
                        ),
                        new model.statement.CompoundStatement(
                                new model.statement.VariableDeclarationStatement(model.type.Type.INTEGER, "v"),
                                new model.statement.CompoundStatement(
                                        new model.statement.IfStatement(
                                                new model.expression.VariableExpression("a"),
                                                new model.statement.AssignmentStatement(
                                                        new model.expression.ConstantExpression(new model.value.IntegerValue(2)),
                                                        "v"
                                                ),
                                                new model.statement.AssignmentStatement(
                                                        new model.expression.ConstantExpression(new model.value.IntegerValue(3)),
                                                        "v"
                                                )
                                        ),
                                        new model.statement.PrintStatement(
                                                new model.expression.VariableExpression("v")
                                        )
                                )
                        )
                )
        );
    }
}