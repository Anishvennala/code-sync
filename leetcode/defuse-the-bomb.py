class Solution {
    public int[] decrypt(int[] code, int k) {
        int n = code.length;
        int[] newArr = new int[n];

        if (k == 0) return newArr;

        int sum = 0;
        int start, end;

        if (k > 0) {
            // Initial window: from index 1 to k
            for (int i = 1; i <= k; i++) {
                sum += code[i % n];
            }

            for (int i = 0; i < n; i++) {
                newArr[i] = sum;
                // Slide window forward
                sum -= code[(i + 1) % n];
                sum += code[(i + k + 1) % n];
            }
        } else { // k < 0
            k = -k;
            // Initial window: from index n - 1 to n - k
            for (int i = 1; i <= k; i++) {
                sum += code[(n - i) % n];
            }

            for (int i = 0; i < n; i++) {
                newArr[i] = sum;
                // Slide window backward
                sum -= code[(n + i - k) % n];
                sum += code[(n + i - 1) % n];
            }
        }

        return newArr;
    }
}