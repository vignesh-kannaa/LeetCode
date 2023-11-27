package Basics;

public class Palindrome {
    public static int reverseNumber(int n){
        int result = 0;
        while (n >0){
            int r = n%10;
            result = result*10+r;
            n = n/10;
        }
        return result;
    }

    public static void main(String[] args){
        int n = 121;
        System.out.print(n == reverseNumber(n));
    }
}
