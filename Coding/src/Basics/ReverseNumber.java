package Basics;

public class ReverseNumber {
    public static int reverseNumber(int n){
//        SOLUTION 1
//        String s = Integer.toString(n);
//        String reverse= "";
//        char[] c = s.toCharArray();
//        for (int i = c.length-1; i >= 0; i--){
//            reverse+=c[i];
//        }
//        int result = Integer.parseInt(reverse);
//        return result;
        int result = 0;
        while (n >0){
            int r = n%10;
            result = result*10+r;
            n = n/10;
        }
        return result;
    }

    public static void main(String[] args){
        int n = 123456;
        System.out.print(reverseNumber(n));
    }
}
