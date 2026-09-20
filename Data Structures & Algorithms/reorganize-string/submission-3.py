class Solution:
    def reorganizeString(self, s: str) -> str:
        count = {}
        for c in s:
            if c in count:
                count[c] += 1
            else:
                count[c] = 1
        
        maxHeap = []
        for c in count:
            maxHeap.append((-count[c], c))
        heapq.heapify(maxHeap)

        hold = None
        res = ""

        while maxHeap or hold:
            if not maxHeap and hold:
                return ""

            cnt, char = heapq.heappop(maxHeap)
            res += char
            cnt += 1

            if hold:
                heapq.heappush(maxHeap, hold)
                hold = None
            
            if cnt != 0:
                hold = (cnt, char)
        
        return res