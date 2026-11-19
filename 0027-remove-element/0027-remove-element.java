class Solution {
    public int removeElement(int[] nums, int val) {
        int index = 0;
        int i = 0;
        while (i < nums.length) {
            if (nums[i] != val) {
                int temp = nums[index];
                nums[index] = nums[i];
                nums[i] = temp;
                index++;
            }
            i++;
        }
        return index;
    }
}