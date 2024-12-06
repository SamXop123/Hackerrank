import java.io.*;
import java.util.*;

public class Solution {

    public static void main(String[] args) {
        
        Scanner sc = new Scanner(System.in);
        
        int size = sc.nextInt();
      
        ArrayList<Integer> list = new ArrayList<>();
        
        for(int i = 0; i<size; i++) {
            int input = sc.nextInt();
            list.add(input);
        }
      
        int queries = sc.nextInt();
        
        for(int j = 0; j < queries; j++) {
            String task = sc.next();
            
            if(task.equals("Insert")) {
                int index = sc.nextInt();
                int element = sc.nextInt();
                
                list.add(index, element);
            }
            
            if(task.equals("Delete")) {
                int index = sc.nextInt();
                list.remove(index);
            }
        }
      
        for (int num : list) {
            System.out.print(num + " "); 
        }
        
        sc.close();
    }
}
