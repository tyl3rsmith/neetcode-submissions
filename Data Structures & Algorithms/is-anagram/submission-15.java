class Solution {
    public boolean isAnagram(String s, String t) {

        char[] sChars = s.toCharArray();
        Arrays.sort(sChars);

        char[] tChars = t.toCharArray();
        Arrays.sort(tChars);

        s = new String(sChars);
        t = new String(tChars);

        return s.equals(t);

    }
}
