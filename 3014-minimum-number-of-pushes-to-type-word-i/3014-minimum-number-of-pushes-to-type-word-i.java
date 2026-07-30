class Solution {
    public int minimumPushes(String word) {
        int n = word.length();
        int ans = 0;
        int t = 8;

        if (n <= 8) {
            return n;
        } else if (n <= 16) {
            int temp = n - 8;
            return (temp * 2) + t;
        } else if (n <= 24) {
            int temp = n - 16;
            return (temp * 3) + 24;
        } else {
            int temp = n - 24;
            return (temp * 4) + 48;
        }
    }
}