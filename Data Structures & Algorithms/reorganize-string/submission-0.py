class Solution:
    def reorganizeString(self, s: str) -> str:
        count = {} # char -> count
        for c in s:
            if c in count:
                count[c] += 1
            else:
                count[c] = 1
            
        maxHeap = []
        for c in count:
            maxHeap.append([-(count[c]), c])
        heapq.heapify(maxHeap)

        prev = None
        res = ""

        while maxHeap or prev:
            if prev and not maxHeap:
                return ""

            # most frequent, except prev
            cnt, char = heapq.heappop(maxHeap)
            res += char
            cnt += 1

            if prev:
                heapq.heappush(maxHeap, prev)
                prev = None
            
            if cnt != 0:
                prev = [cnt, char]

        return res