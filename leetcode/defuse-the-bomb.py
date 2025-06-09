class Solution {
    public int[] decrypt(int[] code, int k) {
        int n = code.length;
        int[]newArr = new int[n];

        //k=0
        if(k==0){
            return newArr;
        }
        int sum = 0;
        //inital window calc
        for(int i = 0; i < k; i++){
            sum += code[i];
        }

        newArr[0] = sum;
        int inputIndex = 1;

        //shift window and continue calc
        for(int i = k; k < n; i++){
            sum += code[i] - code[i - k];
            newArr[inputIndex++] = sum;
        }

        return newArr;
    }
}