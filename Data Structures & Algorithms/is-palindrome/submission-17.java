class Solution {
    private static boolean isAlnum (char c) {
        return ('0' <= c && c <= '9' ||
                'A' <= c  && c <= 'Z' ||
                'a' <= c && c <= 'z');
    }

    public boolean isPalindrome(String s) {
       int l = 0, r = s.length() - 1;

       while (l < r) {
        // skip non alnum chars
        while (l < r && !Solution.isAlnum(s.charAt(l))) {
            l++;
        }

        while (l < r && !Solution.isAlnum(s.charAt(r))) {
            r--;
        }

        if (Character.toLowerCase(s.charAt(l)) != Character.toLowerCase(s.charAt(r))) {
            return false;
        }
        r--;
        l++;
       }
       return true;
    }
}
