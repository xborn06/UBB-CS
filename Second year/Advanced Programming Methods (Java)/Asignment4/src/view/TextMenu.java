package view;

import java.util.HashMap;
import java.util.Map;
import java.util.Scanner;

public class TextMenu {
    private final Map<String, Command> commands = new HashMap<>();

    public void addCommand(Command c) {
        commands.put(c.getKey(), c);
    }

    private void printMenu() {
        System.out.println("\n=== Toy Language Menu ===");
        for (Command com : commands.values()) {
            System.out.printf("%4s : %s%n", com.getKey(), com.getDescription());
        }
        System.out.println("==========================");
    }

    public void show() {
        Scanner scanner = new Scanner(System.in);
        while (true) {
            printMenu();
            System.out.print("Option: ");
            String key = scanner.nextLine();
            Command command = commands.get(key);
            if (command == null) {
                System.out.println("Invalid option!");
            } else {
                command.execute();
            }
        }
    }
}
