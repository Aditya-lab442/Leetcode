
class Solution {
    public String digitSum(String s, int k) {
        while (s.length() > k) {
            String tempStr = "";
            int sum = 0;
            int temp = 0;

            for (int i = 0; i < s.length(); i++) {
                sum += s.charAt(i) - '0';
                temp++;

                if (temp == k) {
                    tempStr += sum;
                    sum = 0;
                    temp = 0;
                }
            }

            if (temp > 0) {
                tempStr += sum;
            }

            s = tempStr;
        }

        return s;
    }
}
