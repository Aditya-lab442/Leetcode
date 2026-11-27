class Solution {
    public List<List<String>> groupAnagrams(String[] strs) {
        Map<String, List> ans = new HashMap<>();

        int fr[] = new int[26];
        for (int i = 0; i < strs.length; i++) {
            Arrays.fill(fr, 0);
            String temp = strs[i];
            for (int j = 0; j < temp.length(); j++) {
                fr[temp.charAt(j) - 'a']++;
            }
            StringBuilder sb = new StringBuilder("");
            for (int j = 0; j < 26; j++) {
                sb.append("#");
                sb.append(fr[j]);
            }
            if (!ans.containsKey(sb.toString())) {
                ans.put(sb.toString(), new ArrayList());
            }
            ans.get(sb.toString()).add(strs[i]);
        }
        return new ArrayList(ans.values());
    }
}