// https://leetcode.com/problems/generate-parentheses/description/
import java.util.List;
import java.util.ArrayList;
import java.lang.StringBuilder;
class Solution {
    public List<String> generateParenthesis(int n) {
        List<String> res = new ArrayList<String>();
        backtrack(n, new StringBuilder(), 0, 0, res);
        return res;
    }

    public void backtrack(int n, StringBuilder s, int close, int open, List<String> res) {
        if (s.length() == 2*n) { //A valid paren pair stirng will always be length 2n
            res.add(s.toString());
            return;
        }

        if (open < n) {
            s.append('(');
            backtrack(n, s, close, open++, res);
            s.deleteCharAt(s.length()-1);
        }

        if (close < open) {
            s.append(')');
            close++;
            backtrack(n, s, close++, open, res);
            s.deleteCharAt(s.length()-1);
        }
    }
}