package view;

public class ExitCommand extends Command {
    public ExitCommand(String key, String description) {
        super(key, description);
    }

    @Override
    public void execute() {
        System.out.println("Exiting Toy Language Interpreter...");
        System.exit(0);
    }
}
