class Solution {
    public int secondHighest(String s) {
        ArrayList<Integer> temp = new ArrayList<>();
        for(int i=0;i<s.length();i++){
            if(Character.isDigit(s.charAt(i))){
                if(!temp.contains(s.charAt(i)-'0')){
                    temp.add(s.charAt(i)-'0');
                }
            }
        }
        if(temp.size()<2){
            return -1;
        }
        int largest = Collections.max(temp);
        int secLarge = -1;
        for(int i=0;i<temp.size();i++){
            if(temp.get(i)>secLarge && temp.get(i)<largest){
                secLarge = temp.get(i);
            }
        }
        return secLarge;
    }
}