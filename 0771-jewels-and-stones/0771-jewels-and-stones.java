class Solution {
    public int numJewelsInStones(String jewels, String stones) {
        int ans = 0;
        for (int i = 0; i < stones.length(); i++) {
            if (jewels.contains(Character.toString(stones.charAt(i)))) {
                ans++;
            }
        }
        return ans;
    }
}