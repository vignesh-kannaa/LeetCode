public class Patterns {
    public static void pattern(int n) {
        for (int r = 0; r < 2*n-1; r++) {
            if (r < n){
                for (int c = 0; c < r + 1; c++) {
                    System.out.print("*");
                }
            }else{
                for (int c = 0; c < 2*n-r-1; c++) {
                    System.out.print("*");
                }
            }
            System.out.println();
        }
    }
    public static void main(String[] args){
        int n = 6;
        pattern(n);
    }
}
/*
  *
 ***
*****

 */