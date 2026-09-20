class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        s_arr = [*s]
        t_arr = [*t]

        s_arr.sort()
        t_arr.sort()

        return s_arr == t_arr