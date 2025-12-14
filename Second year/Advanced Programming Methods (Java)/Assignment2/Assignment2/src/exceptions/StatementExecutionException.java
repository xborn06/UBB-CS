package exceptions;

public class StatementExecutionException extends MyException {
    public StatementExecutionException(String message) {
        super("Statement Execution Error: " + message);
    }
}