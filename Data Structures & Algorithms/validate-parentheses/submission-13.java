class Solution {
    private static String replace(String current, String target, String replacement) {
        StringBuilder sb = new StringBuilder(current);
        int targetLen = target.length();

        int i = 0;
        while (i <= sb.length() - targetLen) {
            if (sb.substring(i, i + targetLen).equals(target)) {
                sb.delete(i, i + targetLen);       // remove target
                sb.insert(i, replacement);         // insert replacement
                i += replacement.length();         // move past inserted text
            } else {
                i++;
            }
        }

        return sb.toString();
    }

    private static boolean contains(String s, String substring) {
        if (substring.length() > s.length()) {
            return false;
        }

        int subLen = substring.length();
        int i = 0;

        while (i <= s.length() - subLen) {
            if (s.substring(i, i + subLen).equals(substring)) {
                return true;
            }
            i++;
        }
        return false;
    }

    public boolean isValid(String s) {
        while (Solution.contains(s, "()") || Solution.contains(s, "[]") || Solution.contains(s, "{}")) {
            s = Solution.replace(s, "()", "");
            s = Solution.replace(s, "{}", "");
            s = Solution.replace(s, "[]", "");
        }
        return s.length() == 0;
    }
}
