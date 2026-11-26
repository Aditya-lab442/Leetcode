class Solution {
    public boolean canAliceWin(int n) {
        if (n < 10) {
            return false;
        }
        int flag = 10;
        while (n > 0) {
            n -= flag;
            if (n < 0 && flag % 2 == 0) {
                return false;
            } else if (n < 0 && flag % 2 != 0) {
                return true;
            }
            if (n == 0 && flag % 2 == 0) {
                return true;
            } else if (n == 0 && flag % 2 != 0) {
                return false;
            }
            flag--;
        }
        return true;
    }
}