class Solution {
public:
    int decode(string s, int i, unordered_map<int, int>& cache) {
        int n = s.length();
        unordered_set<char> valid_digits = {'0', '1', '2', '3', '4', '5', '6'};
        if (i == n) { // base case: found 1 valid decoding
            return 1;
        }

        if (cache.find(i) != cache.end()) {
            return cache[i];
        }
        
        if (s[i] == '0') { // leading digit is a 0
            return 0;
        }

        // if we get here the leading digit isnt a one
        int res = decode(s, i + 1, cache); // take one digit

        // take two digits
        if (i + 1 < n && (s[i] == '1' || (s[i] == '2' && valid_digits.find(s[i + 1]) != valid_digits.end()))) {
            res += decode(s, i + 2, cache);
        }

        cache[i] = res;
        return res;
    }

    int numDecodings(string s) {
        unordered_map<int, int> cache;
        return decode(s, 0, cache);
    }
};
