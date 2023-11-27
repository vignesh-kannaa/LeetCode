package Basics;

public class NumberCount {
    public static int countNumbers(int n){
        /* Solution 1 */
        int count = 0;
        while (n > 0){
            count+=1;
            n = n/10;
        }
        return count;
        /* Solution 2
        String s = Integer.toString(n);
        return s.length(); */
    }
    public static void main(String[] args){
        int n = 12345;
        System.out.println(countNumbers(n));
    }
}
