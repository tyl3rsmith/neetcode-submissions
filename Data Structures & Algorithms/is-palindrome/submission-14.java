class Solution {
    private static boolean isAlnum (char c) {
        return (48 <= c && c <= 57 ||
                65 <= c  && c <= 90 ||
                97 <= c && c <= 122);
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
