class Solution {

    public String encode(List<String> strs) {
        // encode as length + delimiter + string
        StringBuilder sb = new StringBuilder();
        for (String s : strs) {
            sb.append(s.length());
            sb.append('#');
            sb.append(s);
        }
        System.out.println(sb.toString());
        return sb.toString();
    }

    public List<String> decode(String str) {
        List<String> res = new ArrayList<>();
        int i = 0;
        while (i < str.length()) {
            // i will be the start of the string
            // j will read the length and be the end of the string
            // append each substring to res
            int j = i;
            while (str.charAt(j) != '#') { // still digits to read
                j++;
            }
            int length = Integer.parseInt(str.substring(i, j));
            i = j + 1; 
            j = i + length;
            res.add(str.substring(i, j));

            i = j;
        }
        return res;
    }
}
