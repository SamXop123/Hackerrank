import java.util.*;

public class Solution {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);

        int n = sc.nextInt();
        sc.nextLine(); 
        ArrayList<ArrayList<Integer>> data = new ArrayList<>();

        for (int i = 0; i < n; i++) {
            String line = sc.nextLine();
            String[] parts = line.split(" ");  
            ArrayList<Integer> row = new ArrayList<>();
            for (int j = 1; j < parts.length; j++) {  
                row.add(Integer.parseInt(parts[j]));  
            }

            data.add(row);
        }

        int q = sc.nextInt();

        for (int i = 0; i < q; i++) {
            int x = sc.nextInt();  
            int y = sc.nextInt();  

            if (x <= data.size() && y <= data.get(x - 1).size() && x > 0 && y > 0) {
                System.out.println(data.get(x - 1).get(y - 1));  
            } else {
                System.out.println("ERROR!");  
            }
        }

        sc.close();
    }
}
