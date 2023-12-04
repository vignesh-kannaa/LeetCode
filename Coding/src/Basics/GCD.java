package Basics;

public class GCD {
    public static int GCD(int a, int b){
        if (b == 0){
            return a;
        }
        return GCD(b,a%b);
    }

    public static void main(String[] args){
        int a= 4 , b =8;
        System.out.print(GCD(a,b));
    }
}
