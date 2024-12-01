import java.util.Scanner;

public class WordSplitter {
    public static void main(String[] args) {
        Scanner scan = new Scanner(System.in);

        String sentence = scan.nextLine();

        String cleanedSentence = sentence.replaceAll("[\\p{Punct}]+", " ");
        cleanedSentence = cleanedSentence.trim().replaceAll("\\s+", " ");

        String[] words;
        if (cleanedSentence.isEmpty()) {
            words = new String[0];  
        } else {
            words = cleanedSentence.split(" "); 
        }

        System.out.println(words.length);
        for (String word : words) {
            System.out.println(word);
        }

        scan.close();
    }
}
