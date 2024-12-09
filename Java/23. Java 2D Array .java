import java.util.Scanner;

public class Solution {
    public static void main(String[] args) {
        
        Scanner sc = new Scanner(System.in);
        int[][] matrix = new int[6][6];

        for (int i = 0; i < 6; i++) {
            for (int j = 0; j < 6; j++) {
                matrix[i][j] = sc.nextInt();
            }
        }

        int maxSum = Integer.MIN_VALUE;

        for (int i = 1; i < 5; i++) {
            for (int j = 1; j < 5; j++) {
                int hourglassSum = matrix[i - 1][j - 1] + matrix[i - 1][j] + 
                                   matrix[i - 1][j + 1] + matrix[i][j] +
                                   matrix[i + 1][j - 1] + matrix[i + 1][j] + 
                                   matrix[i + 1][j + 1];
                                   
                maxSum = Math.max(maxSum, hourglassSum);
            }
        }

        System.out.println(maxSum);
        sc.close();
    }
}
