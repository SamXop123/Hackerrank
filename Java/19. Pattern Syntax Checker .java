import java.util.Scanner;
import java.util.regex.Pattern;
import java.util.regex.PatternSyntaxException;

public class RegexValidator {
    public static void main(String[] args) {
        Scanner scan = new Scanner(System.in);
        
        int testCases = Integer.parseInt(scan.nextLine());

        for (int i = 0; i < testCases; i++) {
            String input = scan.nextLine();

            try {
                Pattern.compile(input);
                System.out.println("Valid");
            } catch (PatternSyntaxException e) {
                System.out.println("Invalid");
            }
        }

        scan.close();
    }
}
