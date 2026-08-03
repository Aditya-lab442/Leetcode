class Solution {
    public void setZero(int i, int j, int[][] mat) {
        for (int a = 0; a < mat.length; a++) {
            mat[a][j] = 0;
        }
        for (int a = 0; a < mat[i].length; a++) {
            mat[i][a] = 0;
        }
    }

    public void setZeroes(int[][] matrix) {
        ArrayList<ArrayList<Integer>> tempList = new ArrayList<>();
        for (int i = 0; i < matrix.length; i++) {
            for (int j = 0; j < matrix[i].length; j++) {
                if (matrix[i][j] == 0) {
                    ArrayList<Integer> temp = new ArrayList<>();
                    temp.add(i);
                    temp.add(j);
                    tempList.add(temp);
                }
            }
        }
        for (int i = 0; i < tempList.size(); i++) {
            setZero(tempList.get(i).get(0), tempList.get(i).get(1), matrix);
        }
    }
}