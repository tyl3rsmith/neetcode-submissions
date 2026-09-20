class Solution:
    def minInterval(self, intervals: List[List[int]], queries: List[int]) -> List[int]:
        res = []

        for q in queries:
            curr = float('inf')
            for left, right in intervals:
                if left <= q <= right:
                    if right - left + 1 < curr:
                        curr = right - left + 1

            if curr == float('inf'):
                res.append(-1)
            else:
                res.append(curr)

        return res      