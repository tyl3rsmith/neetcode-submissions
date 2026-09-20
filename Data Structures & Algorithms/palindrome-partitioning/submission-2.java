class Solution {
    private boolean isPalindrome(String s, int l, int r) {
        while (l < r) {
            if (s.charAt(l) != s.charAt(r)) {
                return false;
            }
            l++;
            r--;
        }
        return true;
    }

    private void backtrack(String s, int i, List<String> part, List<List<String>> res) {
        if (i >= s.length()) {
            res.add(new ArrayList<>(part));
            return;
        }

        // try every substring from i
        for (int j = i; j < s.length(); j++) {
            // if its a palindrome add it to the partition
            // recur and start to find substrings from one over that are palindromes
            if (isPalindrome(s, i, j)) {
                part.add(s.substring(i, j + 1));
                backtrack(s, j + 1, part, res);
                part.remove(part.size() - 1);
            }
        }
    }

    public List<List<String>> partition(String s) {
        List<List<String>> res = new ArrayList<>();
        List<String> part = new ArrayList<>();
        backtrack(s, 0, part, res);
        return res;
    }
}
