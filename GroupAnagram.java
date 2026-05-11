import java.util.*;

class Solution {
    public List<List<String>> groupAnagrams(String[] strs) {
        Map<String, List<String>> groups = new HashMap<>();

        for (String s : strs) {
            char[] characters = s.toCharArray();
            Arrays.sort(characters);
            
            String key = new String(characters);

            if (!groups.containsKey(key)) {
                groups.put(key, new ArrayList<>());
            }

            groups.get(key).add(s);
        }

        return new ArrayList<>(groups.values());
    }
}