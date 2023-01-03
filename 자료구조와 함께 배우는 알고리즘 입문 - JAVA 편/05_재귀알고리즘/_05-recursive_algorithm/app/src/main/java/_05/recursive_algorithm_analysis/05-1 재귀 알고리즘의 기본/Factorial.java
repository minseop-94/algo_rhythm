package _05.recursive_algorithm;

import java.util.Scanner;

public class Factorial {
    
    // 음이 아닌 정수 n의 팩토리얼 값을 반환
    static int factorial(int n) {
        // if (n > 0)
        //     return n * factorial(n -1);
        // else 
        //     return 1;

        // 조건연산자를 사용한 한 줄 구문
        return (n > 0) ? n * factorial(n - 1) : 1; 
    }

    

    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        
        System.out.println("정수를 입력하세요!! :  ");
        int x = sc.nextInt();

        System.out.println(x + "의 팩토리얼 값은 " + factorial(x) + "입니다");

        sc.close();
    }




}
