import java.util.*;

public class CheckDuplicate {
    static boolean checkDuplicate(int[] arr){
        HashMap <Integer, Integer> m = new HashMap<>();
        for (int n : arr) {
            if(m.containsKey(n)){
                return false;
            }else{
                m.put(n,1);
            }
        }
        return true;
    }
    public static void main(String[] args) {
        int[] nums = {1,2,3,4};
        System.out.println(checkDuplicate(nums));
    }

}
