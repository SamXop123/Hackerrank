
import java.io.*;
import java.util.*;

public class Solution {

    public static void main(String[] args) {
        
        Scanner sc = new Scanner(System.in);
        
        int input = sc.nextInt();
        
        if(input<=100 && input>=(-100)){
            System.out.println("Good job");
        } else{
            System.out.println("Wrong answer");
        }
        
        sc.close();
    }
}
