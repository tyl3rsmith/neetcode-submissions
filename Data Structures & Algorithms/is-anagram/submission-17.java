class Solution {
    public boolean isAnagram(String s, String t) {
        Map<Character, Integer> countS = new HashMap<>();
        Map<Character, Integer> countT = new HashMap<>();

        char[] sChars = s.toCharArray();
        char[] tChars = t.toCharArray();

        for (char charS : sChars) {
            if (countS.containsKey(charS)) {
                countS.put(charS, countS.get(charS) + 1);
            } else {
                countS.put(charS, 1);
            }
        }

        for (char charT : tChars) {
            if (countT.containsKey(charT)) {
                countT.put(charT, countT.get(charT) + 1);
            } else {
                countT.put(charT, 1);
            }
        }

        return countS.equals(countT);
        }
    }
