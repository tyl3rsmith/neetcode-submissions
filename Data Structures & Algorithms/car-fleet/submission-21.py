class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        triplets = []
        for i in range(len(position)):
            triplets.append((position[i], speed[i], (target - position[i])/speed[i]))
        
        triplets.sort(key = lambda x : x[0], reverse=True)
        fleets = []
        for p, s, t in triplets:

            time_to_dest = t
            if fleets and time_to_dest <= fleets[-1]:
                time_to_dest = fleets[-1]
                fleets.pop()
            
            fleets.append(time_to_dest)
        
        return len(fleets)