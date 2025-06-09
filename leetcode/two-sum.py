import java.util.HashMap;

class Solution {
    public int[] twoSum(int[] nums, int target) {
        //key and value pairs are both integers
        HashMap<Integer, Integer> numMap = new HashMap<>();

        for(int i = 0; i < nums.length; i++){
            int matchingPair = target - nums[i];
            if(numMap.containsKey(matchingPair)){
                return new int[] {numMap.get(matchingPair), i};
            }

            numMap.put(nums[i], i);
        }
        return null;
    }
}