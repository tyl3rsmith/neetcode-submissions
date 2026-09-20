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
        
        closestTime = 0
        resIdx = -1

        for i in range(len(self.store[key])):
            time, val = self.store[key][i]
            if time <= timestamp and time > closestTime:
                resIdx = i
        
        return "" if resIdx == -1 else self.store[key][resIdx][1]