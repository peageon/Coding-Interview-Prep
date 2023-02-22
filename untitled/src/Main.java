import java.io.File;
import java.io.FileNotFoundException;
import java.util.Scanner;

public class Main {
    public static String getBiggestNumber(String N, String x, String y) {
        int x_val = Integer.parseInt(x);
        int y_val = Integer.parseInt(y);
        int N_length = N.length();
        int N_first_digit = Character.getNumericValue(N.charAt(0));

        if(N_first_digit > y_val) {
            return new String(new char[N_length]).replace("\0", y);
        }
        else if(N_first_digit == y_val) {
            if(N_length == 1) {
                return y;
            }
            String res = y + getBiggestNumber(N.substring(1), x, y);
            if (res.endsWith("t")) {
                String suffix = new String(new char[N_length - 1]).replace("\0", y);
                return x + suffix;
            } else {
                return res;
            }
        }
        else if(N_first_digit > x_val) {
            String res = new String(new char[N_length - 1]).replace("\0", y);
            return x + res;
        }
        else if(N_first_digit == x_val) {
            if(N_length == 1) {
                return x;
            }
            return x + getBiggestNumber(N.substring(1), x, y);
        }
        else {
            return "t";
        }
    }
    public static void main(String[] args) {
        File file = new File("input.txt");
        //Scanner sc = new Scanner(System.in);
        Scanner sc = null;
        try {
            sc = new Scanner(file);
        } catch (FileNotFoundException e) {
            throw new RuntimeException(e);
        }
        int T;
        T=sc.nextInt();
        sc.nextLine();
        for(int test_case = 1; test_case <= T; test_case++) {
            String[] input = sc.nextLine().split(" ");
            //System.out.println(Arrays.toString(input));
            String N = input[0];
            String x = input[1];
            String y = input[2];
            int min_val = Integer.parseInt(x);
            if (N.length() == 1 && min_val > Character.getNumericValue(N.charAt(0))) {
                System.out.printf("#%d -1%n", test_case);
            }
            else {
                String sol = getBiggestNumber(N, x, y);
                sol = sol.replaceFirst("^0+", "");
                if(sol.endsWith("t")) {
                    sol = new String(new char[N.length() - 1]).replace("\0", y);
                }
                if(sol.equals("")) {
                    sol = "-1";
                }
                System.out.printf("#%d %s%n", test_case, sol);
            }
        }
    }
}