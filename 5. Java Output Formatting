import java.io.*;
import java.util.*;

public class Solution {

    public static void main(String[] args) {
        
        Scanner sc = new Scanner(System.in);
        
        String arrInput[] = new String[3];
        String arrint[] = new String[3];
        String arrSpace[] = new String[3];
        
        for(int i = 0; i<3; i++) {
            arrInput[i] = sc.next(); 
            int integer = sc.nextInt();
            
            if(integer>=10 && integer<100){
                String finalInt1 = "0" + integer;
                arrint[i] = finalInt1;
            }
            else if(integer>=0 && integer<10){
                String finalInt2 = "00" +integer;
                arrint[i] = finalInt2;
            } 
            else if(integer>=100){
                String finalInt3 = "" + integer;
                arrint[i] = finalInt3;
            }
            
            
            int spacesNeeded = 15 - arrInput[i].length();
            String space = " ".repeat(spacesNeeded);
            arrSpace[i] = space;
        }
        
        System.out.println("================================");
        for(int i = 0; i<3; i++) {
            System.out.println(arrInput[i] + arrSpace[i] + arrint[i]);
        }
        System.out.println("================================");
        
        
        sc.close();
        
    }
}



