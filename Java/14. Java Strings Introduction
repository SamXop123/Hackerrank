import java.io.*;
import java.util.*;

public class Solution {

    public static void main(String[] args) {
        
        Scanner sc = new Scanner(System.in);
        String A = sc.next();
        String B = sc.next();
        
        int length = A.length() + B.length();
        System.out.println(length);
        
        int compare = A.compareTo(B);
        if(compare>0) {
            System.out.println("Yes");
        } else {
            System.out.println("No");
        }
        
        String firstA = A.substring(0, 1);
        String lastA = A.substring(1, A.length());
        String capitalA = firstA.toUpperCase();
        
        String firstB = B.substring(0, 1);
        String lastB = B.substring(1, B.length());
        String capitalB = firstB.toUpperCase();
        
        System.out.println(capitalA+lastA +" "+ capitalB+lastB);
        
        sc.close();
    }
}



