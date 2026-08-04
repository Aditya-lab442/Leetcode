class Solution {
    public List<Integer> findMissingElements(int[] nums) {
        List<Integer> ans = new ArrayList<>();
        Arrays.sort(nums);
        int left = 1;
        int i = nums[0] + 1;
        while (left < nums.length) {
            if (i < nums[left]) {
                ans.add(i);
            } else {
                left++;
            }
            i++;
        }
        return ans;
    }
}