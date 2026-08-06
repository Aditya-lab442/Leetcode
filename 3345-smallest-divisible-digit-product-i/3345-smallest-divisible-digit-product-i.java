class Solution {
    public int smallestNumber(int n, int t) {
        int i = n;
        while (true) {
            int temp = i;
            int ans = 1;
            while (temp != 0) {
                ans *= temp % 10;
                temp /= 10;
            }
            if (ans % t == 0) {
                return i;
            }
            i++;
        }
    }
}