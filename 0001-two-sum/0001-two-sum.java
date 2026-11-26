class Solution {
    public int[] twoSum(int[] nums, int target) {
        Map<Integer, Integer> temp = new HashMap<>();
        for (int i = 0; i < nums.length; i++) {
            int diff = target - nums[i];
            if (temp.containsKey(diff)) {
                return new int[] { temp.get(diff), i };
            }
            temp.put(nums[i], i);
        }
        return new int[] { -1, -1 };
    }
}