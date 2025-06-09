class Solution {
    public boolean containsNearbyDuplicate(int[] nums, int k) {
        //set initial window
        for(int i = 0; i < k; i++){
            if(nums[0] == nums[i]){
                return true;
            }
        }

        //slide window
        for(int i = k; i < nums.length; i++){
            if(nums[i] == nums[i - k]){
                return true;
            }
        }
        return false;
    }
}