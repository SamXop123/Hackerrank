import java.io.*;
import java.util.*;

public class Solution {

    public static void main(String[] args) {
        
        Scanner sc = new Scanner(System.in);
        int query = sc.nextInt();
        List<int[]> results = new ArrayList<>();
        
        for (int i = 0; i < query; i++) {
            int a = sc.nextInt();
            int b = sc.nextInt();
            int n = sc.nextInt();
            
            results.add(processSeries(a, b, n));
        }
        sc.close();
        
        for (int[] result : results) {
            for (int num : result) {
                System.out.print(num + " ");
            }
            System.out.println();
        }
    }
    
    public static int[] processSeries(int a, int b, int n) {
        int[] seriesArr = new int[n];  
        int sum = 0;
        
        for (int i = 0; i < n; i++) {
            sum += (int) Math.pow(2, i) * b;  
            seriesArr[i] = a + sum;      
        }
        
        return seriesArr; 
    }
}

