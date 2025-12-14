package exceptions;

public class ExpressionEvaluationException extends MyException {
    public ExpressionEvaluationException(String message) {
        super("Expression Evaluation Error: " + message);
    }
}