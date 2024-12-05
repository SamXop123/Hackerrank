import java.util.Scanner;
import java.util.InputMismatchException;

public class ExceptionHandlingExample {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
          
        try {     
            int x = scanner.nextInt();
            int y = scanner.nextInt(); 
            
            int result = x/y;
    
            if (y == 0) {
                throw new ArithmeticException("/ by zero");
            }
            System.out.println(result);
            
        } catch (InputMismatchException e) {
            System.out.println("java.util.InputMismatchException");
        } catch (NumberFormatException e) {
            System.out.println("java.util.InputMismatchException");
        } catch (ArithmeticException e) {
            System.out.println("java.lang.ArithmeticException: / by zero");
        }
            
        
        
    }
}
