class TimeMap:

    def __init__(self):
        self.store = {} # key -> map of timestamps & values

    def set(self, key: str, value: str, timestamp: int) -> None:
        if key not in self.store:
            self.store[key] = []
            
        self.store[key].append([value, timestamp])

    def get(self, key: str, timestamp: int) -> str:
        if key not in self.store:
            return ""
        
        closest = 0
        resIdx = -1
        for i in range(len(self.store[key])):
            value, time = self.store[key][i]
            if time <= timestamp:
                if time > closest:
                    resIdx = i
                    closest = time
        
        return "" if resIdx == -1 else self.store[key][resIdx][0]

        
