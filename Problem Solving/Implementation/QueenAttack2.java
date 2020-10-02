import java.util.Scanner;

public class QueenAttack {

    public static void main(String args[]) {

        Scanner sc = new Scanner(System.in);
        int n = sc.nextInt();
        int k = sc.nextInt();
        int q_r = sc.nextInt();
        int q_c = sc.nextInt();

        int up = n + 1;
        int down = 0;
        int right = n + 1;
        int left = 0;
        int right_up = q_r + (n-q_c < n-q_r ? n-q_c : n-q_r) + 1;
        int right_down = q_r - (q_r-1 < n-q_c ? q_r-1 : n-q_c) - 1;
        int left_up = q_r + (q_c-1 < n-q_r ? q_c-1 : n-q_r) + 1;
        int left_down = q_r - (q_r-1 < q_c-1 ? q_r-1 : q_c-1) - 1;

        for (int i = 0; i < k; i++) {

            int row = sc.nextInt();
            int col = sc.nextInt();

            if (col == q_c) {
                if (row > q_r && row < up)
                    up = row;
                if (row < q_r && row > down)
                    down = row;
            }

            else if (row == q_r) {
                if (col > q_c && col < right)
                    right = col;
                if (col < q_c && col > left)
                    left = col;
            }

            else if (row - col == q_r - q_c) {
                if (row > q_r && row < right_up)
                    right_up = row;
                if (row < q_r && row > left_down)
                    left_down = row;
            }

            else if (row - q_r == -(col - q_c)) {
                if (row > q_r && row < left_up)
                    left_up = row;
                if (row < q_r && row > right_down)
                    right_down = row;
            }
        }

        int steps = 0;
        steps += up - q_r - 1;
        steps += q_r - down - 1;
        steps += right - q_c - 1;
        steps += q_c - left - 1;
        steps += right_up - q_r - 1;
        steps += q_r - left_down - 1;
        steps += left_up - q_r - 1;
        steps += q_r - right_down - 1;

        System.out.println(steps);
    }
}
