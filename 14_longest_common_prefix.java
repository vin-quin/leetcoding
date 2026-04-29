// https://leetcode.com/problems/longest-common-prefix/
class Solution {
    public String longestCommonPrefix(String[] strs) {
        String prefix = strs[0];

        for (int i = 1; i < strs.length; i++) {
            while (!prefix.isEmpty() && !strs[i].startsWith(prefix)) { // Remove a letter until valid or we empty
                prefix = String.copyValueOf(prefix.toCharArray(), 0, prefix.length()-1);
            }

            if (prefix.isEmpty()) { // No valid prefixes exist
                return prefix;
            }
        }

        return prefix;
    }
}