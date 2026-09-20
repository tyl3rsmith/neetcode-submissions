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
        closestTime = 0
        for i in range(len(self.store[key])):
            val, time = self.store[key][i]
            if time <= timestamp and time > closestTime:
                    closestTime = time
                    resIdx = i

        return "" if resIdx == -1 else self.store[key][resIdx][0]    
