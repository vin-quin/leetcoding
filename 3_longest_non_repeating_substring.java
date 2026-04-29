// https://leetcode.com/problems/longest-substring-without-repeating-characters/description/
class Solution {
    public int lengthOfLongestSubstring(String s) {
        int length=0;
        int l=0,r=0;
        HashSet<Character> seen = new HashSet<>();

        while (r < s.length()) {
            // If window is invalid, shrink left to restore validity
            while (l <= r && seen.contains(s.charAt(r))) {
                seen.remove(s.charAt(l));
                l++;
            }

            seen.add(s.charAt(r));
            length = Math.max(length, r-l+1);

            r++; 
        }

        return length;
    }
}