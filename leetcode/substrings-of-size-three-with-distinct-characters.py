import java.util.HashMap;

class Solution {
    public int countGoodSubstrings(String s) {
        if (s.length() < 3) {
            return 0;
        }
        
        HashMap<Character, Integer> freq = new HashMap<>();
        int k = 3;
        int valid = 0;
        
        // Initialize the first window
        for (int i = 0; i < k; i++) {
            char c = s.charAt(i);
            freq.put(c, freq.getOrDefault(c, 0) + 1);
        }
        
        if (freq.size() == k) {
            valid++;
        }
        
        // Slide the window
        for (int i = k; i < s.length(); i++) {
            char leftChar = s.charAt(i - k);
            // Remove leftChar from the current window
            if (freq.get(leftChar) == 1) {
                freq.remove(leftChar);
            } else {
                freq.put(leftChar, freq.get(leftChar) - 1);
            }
            
            char rightChar = s.charAt(i);
            // Add rightChar to the current window
            freq.put(rightChar, freq.getOrDefault(rightChar, 0) + 1);
            
            // Check if all characters in the current window are distinct
            if (freq.size() == k) {
                valid++;
            }
        }
        
        return valid;
    }
}