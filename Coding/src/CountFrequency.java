import java.util.HashMap;

public class CountFrequency {
    static void checkDuplicate(int[] arr){
        HashMap<Integer, Integer> m = new HashMap<>();
        for (int n : arr) {
            int count = 0 ;
            if(m.containsKey(n))  count = m.get(n);
            m.put(n,1 + count);
        }
        System.out.print(m);
    }
    public static void main(String[] args) {
        int[] nums = {1,2,3,4,1,2,3};
        checkDuplicate(nums);
    }
}
