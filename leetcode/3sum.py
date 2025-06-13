import java.util.*;

class Solution {
    public List<List<Integer>> threeSum(int[] nums) {
        //sort array for non-decr
        Arrays.sort(nums);

        //new list to return
        List<List<Integer>> list = new ArrayList<>();

        for(int i  = 0; i < nums.length; i++){
            if(i > 0 && nums[i] == nums[i - 1]){
                continue;
            }

            int left = i + 1;
            int right = nums.length - 1;
            while(left < right){
                
                int currSum = nums[i] + nums[left] + nums[right];        
                if(currSum == 0){
                    list.add(Arrays.asList(nums[i], nums[left], nums[right]));
                    while (left < right && nums[left] == nums[left + 1]) left++;
                    while (left < right && nums[right] == nums[right - 1]) right--;
                    left++; right--;
                }
                else if(currSum > 0) right--;
                else if(currSum < 0) left++;

            }
        }
        return list;
    }
}