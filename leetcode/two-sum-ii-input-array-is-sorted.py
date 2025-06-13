class Solution {
    public int[] twoSum(int[] numbers, int target) {
        
        int right = numbers.length - 1;
        int left = 0;
        while(left < right){
            int currSum = numbers[left] + numbers[right];
            if(currSum == target){
                return new int[]{left+1, right+1};
            }

            if(currSum < target) left++;
            if(currSum > target) right--;
        }
        return new int[]{0};
    }
}