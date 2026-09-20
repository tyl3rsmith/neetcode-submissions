class Solution {
    public String minWindow(String s, String t) {
        if (t.isEmpty()) {
            return "";
        }

        Map<Character, Integer> countT = new HashMap<>();
        for (char c : t.toCharArray()) {
            countT.put(c, countT.getOrDefault(c, 0) + 1);
        }
        
        int[] res = new int[2];
        int resLen = Integer.MAX_VALUE;

        for (int i = 0; i < s.length(); i++) {
            Map<Character, Integer> window = new HashMap<>();
            for (int j = i; j < s.length(); j++) {
                // add character to window
                window.put(s.charAt(j), window.getOrDefault(s.charAt(j), 0) + 1);

                boolean flag = true;
                // check if the window doesnt match countT
                for (char c : countT.keySet()) {
                    if (countT.get(c) > window.getOrDefault(c, 0)) {
                        flag = false;
                        break;
                    }
                }

                // if the window matches update the res only if its smaller
                if (flag && (j - i + 1) < resLen) {
                    res = new int[]{i, j};
                    resLen = j - i + 1;
                }
            }
        }

        return resLen == Integer.MAX_VALUE ? "" : s.substring(res[0], res[1] + 1);
    }
}
