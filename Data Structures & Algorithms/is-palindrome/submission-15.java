class Solution {
    private static boolean isAlnum (char c) {
        return ('0' <= c && c <= '9' ||
                'A' <= c  && c <= 'Z' ||
                'a' <= c && c <= 'z');
    }

    public boolean isPalindrome(String s) {
        StringBuilder newStr = new StringBuilder();
        for (char c : s.toCharArray()) {
            if (Solution.isAlnum(c)) {
                newStr.append(Character.toLowerCase(c));
            }
        }

        return newStr.toString().equals(newStr.reverse().toString());
    }
}
