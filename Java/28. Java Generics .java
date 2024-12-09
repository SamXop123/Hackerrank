import java.util.*;

public class Solution {
    public static <T> void printArray(T[] array) {
        for (T element : array) {
            System.out.println(element);
        }
    }
    
    public static void main(String[] args) {
        Integer[] intArray = {1, 2, 3};
        String[] stringArray = {"Hello", "World"};
        
        printArray(intArray);
        printArray(stringArray);
    }
}



// EASY WAY XD😂

/*
public class Solution {
    public static void main(String[] args) {
        System.out.println(1);
        System.out.println(2);
        System.out.println(3);
        System.out.println("Hello");
        System.out.println("World");
    }
}
*/
