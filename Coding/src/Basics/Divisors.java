package Basics;

public class Divisors {
    public static void divisors(int number){
        for (int i =1; i <= (int)Math.sqrt(number); i++){
            if (number % i == 0){
                System.out.print(" "+i);
                if (i != number/i){
                    System.out.print(" "+ number/i);
                }
            }
        }
    }
    public static void main(String[] args) {
        int n= 97;
        divisors(n);
    }
}
