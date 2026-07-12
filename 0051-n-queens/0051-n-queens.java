class Solution {
    public void placeQueens(int col, List<List<String>> ans, List<String> board, int[] left, int[] lower, int[] upper,
            int n) {
        if (col == n) {
            ans.add(new ArrayList<>(board));
            ;
            return;
        }
        for (int row = 0; row < n; row++) {
            if (left[row] == 0 && lower[row + col] == 0 && upper[n - 1 + col - row] == 0) {
                char[] temp = board.get(row).toCharArray();
                temp[col] = 'Q';
                board.set(row, new String(temp));
                left[row] = 1;
                lower[row + col] = 1;
                upper[n - 1 + col - row] = 1;
                placeQueens(col + 1, ans, board, left, lower, upper, n);
                temp = board.get(row).toCharArray();
                temp[col] = '.';
                board.set(row, new String(temp));
                left[row] = 0;
                lower[row + col] = 0;
                upper[n - 1 + col - row] = 0;
            }
        }
    }

    public List<List<String>> solveNQueens(int n) {
        List<List<String>> ans = new ArrayList<>();
        List<String> board = new ArrayList<>();

        // Initialize board with "...."
        StringBuilder sb = new StringBuilder();
        for (int i = 0; i < n; i++) {
            sb.append('.');
        }

        for (int i = 0; i < n; i++) {
            board.add(sb.toString());
        }

        int[] left = new int[n];
        int[] lower = new int[2 * n - 1];
        int[] upper = new int[2 * n - 1];

        placeQueens(0, ans, board, left, lower, upper, n);

        return ans;
    }
}