class Solution {

    public String encode(List<String> strs) {
        StringBuilder res = new StringBuilder();
        for (String s : strs) {
            res.append(s.length());
            res.append('#');
            res.append(s);
        }
        return res.toString();
    }

    public List<String> decode(String str) {
        List<String> res = new ArrayList<>();
        int i = 0;

        while (i < str.length()) {
            int j = i;
            while (str.charAt(j) != '#') {
                j++;
            }
            int length = Integer.parseInt(str.substring(i, j));

            i = j + 1; // j is at the # so move the pointer to read chars
            j = i + length; // j now points to the next num to read
            res.add(str.substring(i, j));
            i = j;
        }
        return res;
    }
}
