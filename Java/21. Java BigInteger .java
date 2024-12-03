import java.io.*;
import java.util.*;
import java.text.*;
import java.math.*;
import java.util.regex.*;

public class Solution {

    public static void main(String[] args) {
        
        Scanner sc = new Scanner(System.in);
        
        BigInteger a = sc.nextBigInteger();
        BigInteger b = sc.nextBigInteger();
        
        BigInteger adding = a.add(b);
        BigInteger mult = a.multiply(b);
        
        System.out.println(adding);
        System.out.println(mult);
        
        sc.close();
    }
}
