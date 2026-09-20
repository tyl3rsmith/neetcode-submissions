class TimeMap:

    def __init__(self):
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
        
        closest = 0
        for time in self.store[key]:
            if time <= timestamp:
                closest = max(closest, time)
        
        return "" if closest == 0 else self.store[key][closest][-1]