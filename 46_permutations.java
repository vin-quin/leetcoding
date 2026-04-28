
/**
 * https://leetcode.com/problems/permutations/description/
 */
import java.util.ArrayList;
import java.util.List;

class Solution {

    public List<List<Integer>> solve(int[] nums) {
        List<List<Integer>> res = new ArrayList<>();
        boolean[] used = new boolean[nums.length];
        backtrack(nums, res, new ArrayList<Integer>(), used);
        return res;
    }

    public void backtrack(int[] nums,  List<List<Integer>> res, List<Integer> perm, boolean[] used) {
        if (perm.size() == nums.length) {
            res.add(new ArrayList<>(perm));
            return;
        }

        for (int i = 0; i < nums.length; i++) {
            if (!used[i]) {
                used[i] = true;
                perm.add(nums[i]);
                backtrack(nums, res, perm, used);

                perm.remove(perm.size() - 1); // Remove the last number we added in the permutation and go next
                used[i] = false;
            }
        }

    }
}

public class Main {

    public static void main(String[] args) {
        Solution s = new Solution();
        System.out.println(s.solve(new int[]{1, 2, 3}));
    }
}
