class Solution:
    def isAnagram(self, s: str, t: str) -> bool:

        if len(s) != len(t):
            return False
        
        table_one = {}
        table_two = {}

        for char in s:
            if char in table_one:
                table_one[char] += 1
            else:
                table_one[char] = 1

        for char in t:
            if char in table_two:
                table_two[char] += 1
            else:
                table_two[char] = 1
        
        for key in table_one:
            if key not in table_two:
                return False

            if table_two[key] != table_one[key]:
                return False     
            
        return True