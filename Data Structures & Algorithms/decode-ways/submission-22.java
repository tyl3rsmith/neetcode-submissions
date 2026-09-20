class Solution {
    public int numDecodings(String s) {
        int dp1 = 0; // last digit
        int dp2 = 1; // at length of s
        int dp3 = 0; // 2 past the last digit

        for (int i = s.length() - 1; i >= 0; i--) {
            if (s.charAt(i) == '0') {
                dp1 = 0;
            } else {
                dp1 = dp2;

                if (i + 1 < s.length()) {
                    if (s.charAt(i) == '1' || s.charAt(i) == '2' && s.charAt(i + 1) < '7') {
                        dp1 += dp3;
                    }
            }
            }
            dp3 = dp2;
            dp2 = dp1;
            dp1 = 0;
        }

        return dp2;
    }
}
