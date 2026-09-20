class TimeMap:

    def __init__(self):
        self.store = {} # schema: key -> [val, time]

    def set(self, key: str, value: str, timestamp: int) -> None:
        if key in self.store: # we already set this key before
            self.store[key].append([value, timestamp])
        else: # first time setting this key
            self.store[key] = [[value, timestamp]]

    def get(self, key: str, timestamp: int) -> str:
        if key not in self.store:
            return ""

        resIdx = -1
        l, r = 0, len(self.store[key]) - 1

        while l <= r:
            m = l + (r - l) // 2
            val, time = self.store[key][m]

            if time < timestamp:
                # this is a potential result but we want to maximize so move right
                resIdx = m
                l = m + 1
            
            elif time == timestamp:
                resIdx = m
                break
            
            else: # the time is too large need to shrink towards the left
                r = m - 1
        
        return "" if resIdx == -1 else self.store[key][resIdx][0]