class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        triplets = []
        for i in range(len(position)):
            triplets.append((position[i], speed[i], (target - position[i])/speed[i]))
        
        triplets.sort(key = lambda x : x[0], reverse=True)
        fleets = []
        for p, s, t in triplets:
            fleets.append(t)
            if len(fleets) >= 2 and fleets[-1] <= fleets[-2]:
                fleets.pop()
        
        return len(fleets)