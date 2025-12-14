import controller.Controller;
import controller.ControllerImpl;
import repository.Repository;
import repository.RepositoryImpl;
import view.TextView;

public class Main {
    public static void main(String[] args) {
        Repository repository = new RepositoryImpl();

        Controller controller = new ControllerImpl(repository);

        TextView textView = new TextView(controller);
        textView.run();
    }
}