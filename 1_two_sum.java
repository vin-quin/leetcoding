class Solution {
    public int[] twoSum(int[] nums, int target) {
        HashMap<Integer,Integer> m = new HashMap<>(); // N:idx
        int[] res = new int[]{0, nums.length-1};

        for (int i = 0; i < nums.length; i++)  {
            int need = target-nums[i];
            if (m.containsKey(need)) {
                res[0] = i;
                res[1] = m.get(need);
                return res;
            }

            m.put(nums[i], i);
        }

        return res;
    }
}