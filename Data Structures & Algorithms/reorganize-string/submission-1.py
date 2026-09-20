class Solution:
    def reorganizeString(self, s: str) -> str:
        count = {} # char -> freq
        for c in s:
            if c in count:
                count[c] += 1
            else:
                count[c] = 1
        
        # maxHeap for efficient max lookup
        maxHeap = []
        for c in count:
            maxHeap.append((-count[c], c))
        heapq.heapify(maxHeap)

        on_hold = None
        res = ""

        while on_hold or maxHeap: # we still have characters to add
            if on_hold and not maxHeap: # we used all the chars we can add but there's still chars on hold waiting to be added
                return ''
            
            cnt, char = heapq.heappop(maxHeap)
            res += char
            cnt += 1

            if on_hold:
                heapq.heappush(maxHeap, on_hold)
                on_hold = None

            if cnt != 0:
                on_hold = (cnt, char)

        return res

        