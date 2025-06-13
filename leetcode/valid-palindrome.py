class Solution {
    public boolean isPalindrome(String s) {
        //first filter string s
        String cleaned = s.replaceAll("[^a-zA-Z0-9]", "");

        //use pointers
        int right = cleaned.length() - 1;
        int left = 0;
        while(left < right){
            if((Character.toLowerCase(cleaned.charAt(left))) == Character.toLowerCase(cleaned.charAt(right))){
                left++;
                right--;
            }
            else{
                return false;
            }
        }
        return true;
    }
}