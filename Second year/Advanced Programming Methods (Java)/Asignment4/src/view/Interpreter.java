package view;

import controller.ControllerImpl;
import model.expression.*;
import model.state.*;
import model.statement.*;
import model.value.BooleanValue;
import model.value.IntegerValue;
import model.value.StringValue;
import repository.RepositoryImpl;

import java.util.Scanner;

public class Interpreter {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        System.out.print("Enter log file base name (e.g. log): ");
        String baseName = scanner.nextLine().trim();
        if (baseName.isEmpty())
            baseName = "log";

        Statement ex1 = new CompoundStatement(
                new VariableDeclarationStatement(new model.type.IntType(), "v"),
                new CompoundStatement(
                        new AssignmentStatement(new ConstantExpression(new IntegerValue(2)), "v"),
                        new PrintStatement(new VariableExpression("v"))
                )
        );
        ProgramState prg1 = new ProgramState(new StackExecutionStack(), new MapSymbolTable(), new ListOut(), new MapFileTable(), ex1);
        RepositoryImpl repo1 = new RepositoryImpl(baseName + "1.txt");
        repo1.addProgram(prg1);
        ControllerImpl ctr1 = new ControllerImpl(repo1);

        Statement ex2 = new CompoundStatement(
                new VariableDeclarationStatement(new model.type.IntType(), "a"),
                new CompoundStatement(
                        new AssignmentStatement(
                                new BinaryOperatorExpression(
                                        "+",
                                        new ConstantExpression(new IntegerValue(2)),
                                        new BinaryOperatorExpression(
                                                "*",
                                                new ConstantExpression(new IntegerValue(3)),
                                                new ConstantExpression(new IntegerValue(5))
                                        )
                                ),
                                "a"
                        ),
                        new CompoundStatement(
                                new VariableDeclarationStatement(new model.type.IntType(), "b"),
                                new CompoundStatement(
                                        new AssignmentStatement(
                                                new BinaryOperatorExpression(
                                                        "+",
                                                        new BinaryOperatorExpression(
                                                                "-",
                                                                new VariableExpression("a"),
                                                                new BinaryOperatorExpression(
                                                                        "/",
                                                                        new ConstantExpression(new IntegerValue(4)),
                                                                        new ConstantExpression(new IntegerValue(2))
                                                                )
                                                        ),
                                                        new ConstantExpression(new IntegerValue(7))
                                                ),
                                                "b"
                                        ),
                                        new PrintStatement(new VariableExpression("b"))
                                )
                        )
                )
        );
        ProgramState prg2 = new ProgramState(new StackExecutionStack(), new MapSymbolTable(), new ListOut(), new MapFileTable(), ex2);
        RepositoryImpl repo2 = new RepositoryImpl(baseName + "2.txt");
        repo2.addProgram(prg2);
        ControllerImpl ctr2 = new ControllerImpl(repo2);

        Statement ex3 = new CompoundStatement(
                new VariableDeclarationStatement(new model.type.BoolType(), "a"),
                new CompoundStatement(
                        new AssignmentStatement(new ConstantExpression(new BooleanValue(false)), "a"),
                        new CompoundStatement(
                                new VariableDeclarationStatement(new model.type.IntType(), "v"),
                                new CompoundStatement(
                                        new IfStatement(
                                                new VariableExpression("a"),
                                                new AssignmentStatement(new ConstantExpression(new IntegerValue(2)), "v"),
                                                new AssignmentStatement(new ConstantExpression(new IntegerValue(3)), "v")
                                        ),
                                        new PrintStatement(new VariableExpression("v"))
                                )
                        )
                )
        );
        ProgramState prg3 = new ProgramState(new StackExecutionStack(), new MapSymbolTable(), new ListOut(), new MapFileTable(), ex3);
        RepositoryImpl repo3 = new RepositoryImpl(baseName + "3.txt");
        repo3.addProgram(prg3);
        ControllerImpl ctr3 = new ControllerImpl(repo3);

        Statement ex4 = new CompoundStatement(
                new VariableDeclarationStatement(new model.type.StringType(), "varf"),
                new CompoundStatement(
                        new AssignmentStatement(new ConstantExpression(new StringValue("test.in")), "varf"),
                        new CompoundStatement(
                                new OpenRFileStatement(new VariableExpression("varf")),
                                new CompoundStatement(
                                        new VariableDeclarationStatement(new model.type.IntType(), "varc"),
                                        new CompoundStatement(
                                                new ReadFileStatement(new VariableExpression("varf"), "varc"),
                                                new CompoundStatement(
                                                        new PrintStatement(new VariableExpression("varc")),
                                                        new CompoundStatement(
                                                                new ReadFileStatement(new VariableExpression("varf"), "varc"),
                                                                new CompoundStatement(
                                                                        new PrintStatement(new VariableExpression("varc")),
                                                                        new CloseRFileStatement(new VariableExpression("varf"))
                                                                )
                                                        )
                                                )
                                        )
                                )
                        )
                )
        );
        ProgramState prg4 = new ProgramState(new StackExecutionStack(), new MapSymbolTable(), new ListOut(), new MapFileTable(), ex4);
        RepositoryImpl repo4 = new RepositoryImpl(baseName + "4.txt");
        repo4.addProgram(prg4);
        ControllerImpl ctr4 = new ControllerImpl(repo4);

        Statement ex5 = new CompoundStatement(
                new VariableDeclarationStatement(new model.type.RefType(new model.type.IntType()), "v"),
                new CompoundStatement(
                        new HeapAllocationStatement("v", new ConstantExpression(new IntegerValue(20))),
                        new CompoundStatement(
                                new VariableDeclarationStatement(new model.type.RefType(new model.type.RefType(new model.type.IntType())), "a"),
                                new CompoundStatement(
                                        new HeapAllocationStatement("a", new VariableExpression("v")),
                                        new CompoundStatement(
                                                new PrintStatement(new VariableExpression("v")),
                                                new PrintStatement(new VariableExpression("a"))
                                        )
                                )
                        )
                )
        );
        ProgramState prg5 = new ProgramState(new StackExecutionStack(), new MapSymbolTable(), new ListOut(), new MapFileTable(), ex5);
        RepositoryImpl repo5 = new RepositoryImpl(baseName + "5.txt");
        repo5.addProgram(prg5);
        ControllerImpl ctr5 = new ControllerImpl(repo5);

        Statement ex6 = new CompoundStatement(
                new VariableDeclarationStatement(new model.type.RefType(new model.type.IntType()), "v"),
                new CompoundStatement(
                        new HeapAllocationStatement("v", new ConstantExpression(new IntegerValue(20))),
                        new CompoundStatement(
                                new VariableDeclarationStatement(new model.type.RefType(new model.type.RefType(new model.type.IntType())), "a"),
                                new CompoundStatement(
                                        new HeapAllocationStatement("a", new VariableExpression("v")),
                                        new CompoundStatement(
                                                new PrintStatement(new HeapReadExpression(new VariableExpression("v"))),
                                                new PrintStatement(
                                                        new BinaryOperatorExpression(
                                                                "+",
                                                                new HeapReadExpression(new HeapReadExpression(new VariableExpression("a"))),
                                                                new ConstantExpression(new IntegerValue(5))
                                                        )
                                                )
                                        )
                                )
                        )
                )
        );
        ProgramState prg6 = new ProgramState(new StackExecutionStack(), new MapSymbolTable(), new ListOut(), new MapFileTable(), ex6);
        RepositoryImpl repo6 = new RepositoryImpl(baseName + "6.txt");
        repo6.addProgram(prg6);
        ControllerImpl ctr6 = new ControllerImpl(repo6);

        Statement ex7 = new CompoundStatement(
                new VariableDeclarationStatement(new model.type.RefType(new model.type.IntType()), "v"),
                new CompoundStatement(
                        new HeapAllocationStatement("v", new ConstantExpression(new IntegerValue(20))),
                        new CompoundStatement(
                                new PrintStatement(new HeapReadExpression(new VariableExpression("v"))),
                                new CompoundStatement(
                                        new HeapWriteStatement("v", new ConstantExpression(new IntegerValue(30))),
                                        new PrintStatement(
                                                new BinaryOperatorExpression(
                                                        "+",
                                                        new HeapReadExpression(new VariableExpression("v")),
                                                        new ConstantExpression(new IntegerValue(5))
                                                )
                                        )
                                )
                        )
                )
        );
        ProgramState prg7 = new ProgramState(new StackExecutionStack(), new MapSymbolTable(), new ListOut(), new MapFileTable(), ex7);
        RepositoryImpl repo7 = new RepositoryImpl(baseName + "7.txt");
        repo7.addProgram(prg7);
        ControllerImpl ctr7 = new ControllerImpl(repo7);

        Statement ex8 = new CompoundStatement(
                new VariableDeclarationStatement(new model.type.RefType(new model.type.IntType()), "v"),
                new CompoundStatement(
                        new HeapAllocationStatement("v", new ConstantExpression(new IntegerValue(20))),
                        new CompoundStatement(
                                new VariableDeclarationStatement(new model.type.RefType(new model.type.RefType(new model.type.IntType())), "a"),
                                new CompoundStatement(
                                        new HeapAllocationStatement("a", new VariableExpression("v")),
                                        new CompoundStatement(
                                                new HeapAllocationStatement("v", new ConstantExpression(new IntegerValue(30))),
                                                new PrintStatement(
                                                        new HeapReadExpression(
                                                                new HeapReadExpression(new VariableExpression("a"))
                                                        )
                                                )
                                        )
                                )
                        )
                )
        );
        ProgramState prg8 = new ProgramState(new StackExecutionStack(), new MapSymbolTable(), new ListOut(), new MapFileTable(), ex8);
        RepositoryImpl repo8 = new RepositoryImpl(baseName + "8.txt");
        repo8.addProgram(prg8);
        ControllerImpl ctr8 = new ControllerImpl(repo8);

        Statement ex9 = new CompoundStatement(
                new VariableDeclarationStatement(new model.type.IntType(), "v"),
                new CompoundStatement(
                        new AssignmentStatement(new ConstantExpression(new IntegerValue(4)), "v"),
                        new CompoundStatement(
                                new WhileStatement(
                                        new BinaryOperatorExpression(
                                                ">",
                                                new VariableExpression("v"),
                                                new ConstantExpression(new IntegerValue(0))
                                        ),
                                        new CompoundStatement(
                                                new PrintStatement(new VariableExpression("v")),
                                                new AssignmentStatement(
                                                        new BinaryOperatorExpression(
                                                                "-",
                                                                new VariableExpression("v"),
                                                                new ConstantExpression(new IntegerValue(1))
                                                        ),
                                                        "v"
                                                )
                                        )
                                ),
                                new PrintStatement(new VariableExpression("v"))
                        )
                )
        );
        ProgramState prg9 = new ProgramState(new StackExecutionStack(), new MapSymbolTable(), new ListOut(), new MapFileTable(), ex9);
        RepositoryImpl repo9 = new RepositoryImpl(baseName + "9.txt");
        repo9.addProgram(prg9);
        ControllerImpl ctr9 = new ControllerImpl(repo9);

        TextMenu menu = new TextMenu();
        menu.addCommand(new ExitCommand("0", "Exit the interpreter"));
        menu.addCommand(new RunExample("1", ex1.toString(), ctr1));
        menu.addCommand(new RunExample("2", ex2.toString(), ctr2));
        menu.addCommand(new RunExample("3", ex3.toString(), ctr3));
        menu.addCommand(new RunExample("4", ex4.toString(), ctr4));
        menu.addCommand(new RunExample("5", ex5.toString(), ctr5));
        menu.addCommand(new RunExample("6", ex6.toString(), ctr6));
        menu.addCommand(new RunExample("7", ex7.toString(), ctr7));
        menu.addCommand(new RunExample("8", ex8.toString(), ctr8));
        menu.addCommand(new RunExample("9", ex9.toString(), ctr9));
        menu.show();
    }
}
