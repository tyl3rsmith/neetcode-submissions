class Solution:
    def minInterval(self, intervals: List[List[int]], queries: List[int]) -> List[int]:
        res = []
        for q in queries:
            curr = -1
            for left, right in intervals:
                if left <= q <= right:
                    if curr == -1 or right - left + 1 < curr:
                        curr = right - left + 1

            res.append(curr)
        return res      