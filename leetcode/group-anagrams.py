import java.util.HashMap;

class Solution {
    public List<List<String>> groupAnagrams(String[] strs) {
        HashMap<String, String> map = new HashMap<>();

        for(int i  = 0; i < strs.length; i++){
            char[] arr = str.toCharArray();
            Arrays.sort(arr);
            String sorted = new String(arr);

            if(!map.containsKey(sorted)){
                //key not in map
                map.put(sorted, strs[i]);
            }
            else{
                //key in map already
                map.get(sorted).add(sorted);
            }

        }

        return map.values();
    }
}