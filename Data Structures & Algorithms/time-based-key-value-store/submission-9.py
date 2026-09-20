class TimeMap:

    def __init__(self):
        # hashmap : key -> hashmap -> timestamp, list of values
        self.store = {}

    def set(self, key: str, value: str, timestamp: int) -> None:
        if key not in self.store:
            self.store[key] = {}
        if timestamp not in self.store[key]:
            self.store[key][timestamp] = []

        self.store[key][timestamp].append(value)
        
    def get(self, key: str, timestamp: int) -> str:
        if key not in self.store:
            return ""
        
        closestTime = 0
        for time in self.store[key]:
            if time <= timestamp:
                closestTime = max(closestTime, time)
        
        return "" if closestTime == 0 else self.store[key][closestTime][-1]