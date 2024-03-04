import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.*;

public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

        int k = Integer.parseInt(br.readLine());
        int n = Integer.parseInt(br.readLine());

        char[] upperLine = new char[k];
        for (int i=0; i < k; i++) {
            upperLine[i] = (char) ('A' + i);
        }
        char[] lowerLine = br.readLine().toCharArray();

        char[][] board = new char[n][k-1];
        int changeIndex = 0;
        for(int i = 0; i < n; i++) {
            board[i] = br.readLine().toCharArray();
            if (board[i][0] == '?') {
                changeIndex = i;
            }
        }

        for (int i = 0; i < changeIndex; i++) {
            for (int j = 0; j < k - 1; j++) {
                if (board[i][j] == '-') {
                    char temp = upperLine[j];
                    upperLine[j] = upperLine[j+1];
                    upperLine[j+1] = temp;
                }
            }
        }

        for (int i = n-1; i > changeIndex; i--) {
            for (int j = 0; j < k - 1; j++) {
                if (board[i][j] == '-') {
                    char temp = lowerLine[j];
                    lowerLine[j] = lowerLine[j+1];
                    lowerLine[j+1] = temp;
                }
            }
        }

        StringBuilder res = new StringBuilder();

        for (int i = 0; i < k-1; i++) {
            if (upperLine[i] == lowerLine[i]) {
                res.append("*");
            }
            else if (upperLine[i] == lowerLine[i+1]) {
                if(upperLine[i+1] != lowerLine[i]) {
                    for(int a=0; a < k-1; a++) {
                        System.out.print("x");
                    }
                    return;
                }
                res.append("-");
                if (i < k-2) res.append("*");
                i++;
            }
            else {
                for(int a=0; a < k-1; a++) {
                    System.out.print("x");
                }
                return;
            }
        }
        System.out.println(res);

    }
}