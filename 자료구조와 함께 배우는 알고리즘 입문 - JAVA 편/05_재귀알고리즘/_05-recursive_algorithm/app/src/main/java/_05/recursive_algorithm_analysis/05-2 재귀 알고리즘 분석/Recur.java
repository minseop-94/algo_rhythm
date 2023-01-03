package _05.recursive_algorithm_analysis;

import java.util.Scanner;

public class Recur {

    // 재귀 함수 
    static void recur(int n) {
        if (n > 0) {
            recur(n -1);
        }
    }

    // 꼬리 재귀를 제거 
    static void recur2(int n) {
        while (n > 0) {
            recur(n -1);
            System.out.println(n);
            n = n - 2;
        }
    }

    // 재귀를 제거 
    static void recur3(int n) {
        IntStack s = new IntStack(n); // stack 형태의 자료구조 

        while (true) {
            if (n > 0) {
                s.push(n);
                n = n - 1;
                continue;
            }
            if (s.isEmpty() != true) {
                n = s.pop();
                System.out.println(n);
                n = n -2;
                continue;
            }
            break;
        }

    }

    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);

        System.out.println("정수를 입력하세요!! : ");
        int x = sc.nextInt();

        recur(x);
    }
}
