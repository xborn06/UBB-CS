package exceptions;

public class ADTException extends MyException {
    public ADTException(String message) {
        super("ADT Error: " + message);
    }
}