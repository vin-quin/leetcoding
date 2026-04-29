// https://leetcode.com/problems/generate-parentheses/description/
import java.util.List;
import java.util.ArrayList;
class Solution {
    public List<String> generateParenthesis(int n) {
        List<String> res = new ArrayList<String>();
        backtrack(n, "", 0, 0, res);
        return res;
    }

    public void backtrack(int n, StringBuilder s, int close, int open, List<String> res) {
        if (s.length() == 2*n) { //A valid paren pair stirng will always be length 2n
            res.add(s);
            return;
        }

        if (open < n) {
            backtrack(n, s+'(', close, open+1, res);
        }

        if (close < open) {
            backtrack(n, s+')', close+1, open, res);
        }
    }
}