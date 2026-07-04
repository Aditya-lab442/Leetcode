class Solution {
    public void heapify(int[] arr, int n, int i) {
        int left = i * 2 + 1;
        int right = i * 2 + 2;
        int largest = i;
        if (left < n && arr[left] > arr[largest])
            largest = left;
        if (right < n && arr[right] > arr[largest])
            largest = right;
        if (largest != i) {
            int temp = arr[i];
            arr[i] = arr[largest];
            arr[largest] = temp;
            heapify(arr, n, largest);
        }
    }

    public int[] sortArray(int[] nums) {
        int n = nums.length;
        for (int i = n / 2 - 1; i >= 0; i--)
            heapify(nums, n, i);
        for (int j = n - 1; j >= 0; j--) {
            int temp = nums[0];
            nums[0] = nums[j];
            nums[j] = temp;
            heapify(nums, j, 0);
        }
        return nums;
    }
}