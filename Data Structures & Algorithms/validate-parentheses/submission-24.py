class Solution:
    def isValid(self, s: str) -> bool:
        # brute force approach:
        # for each set of brackets
        # while s contains at least one of them we keep removing it
        # repeat this until the string is empty (True) or there are brackets left (False)

        while '[]' in s or '{}' in s or '()' in s:
            s = s.replace('[]', '')
            s = s.replace('{}', '')
            s = s.replace('()', '')
        
        return True if s == '' else False


