class Solution {
    public void rotate(int[] nums, int k) {
        k = k % nums.length;
        int[] temp1 = new int[nums.length - k];
        int[] temp2 = new int[k];
        for (int i = 0; i < nums.length - k; i++) {
            temp1[i] = nums[i];
        }
        int j = 0;
        for (int i = nums.length - k; i < nums.length; i++) {
            temp2[j] = nums[i];
            j++;
        }
        int i = 0;
        for (i = 0; i < k; i++) {
            nums[i] = temp2[i];
        }
        j = 0;
        for (i = k; i < nums.length; i++) {
            nums[i] = temp1[j];
            j++;
        }
    }
}