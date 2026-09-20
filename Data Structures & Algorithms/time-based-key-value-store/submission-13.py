class TimeMap:

    def __init__(self):
        # hashmap : key -> [time, val]
        self.store = {}

    def set(self, key: str, value: str, timestamp: int) -> None:
        if key not in self.store:
            self.store[key] = []

        self.store[key].append([timestamp, value])
        
    def get(self, key: str, timestamp: int) -> str:
        if key not in self.store:
            return ""
        
        res = ""
        l, r = 0, len(self.store[key]) - 1

        while l <= r:
            m = l + (r - l) // 2
            time, val = self.store[key][m]

            if time > timestamp: # time too big search left
                r = m - 1
            else:
                res = self.store[key][m][1]
                l = m + 1
        
        return res