class Solution:
    # costs[i] = cost of pass for 1, 7, 30 days
    # pass starts day of

    # return min cost needed to travel every day in the given list of days
    def mincostTickets(self, days: List[int], costs: List[int]) -> int:
        memo = {}

        def dfs(i):
            if i >= len(days):
                return 0
            
            if i in memo:
                return memo[i]

            # take a 1 day pass
            new_day = days[i] + 1
            next_index = 0
            
            for j in range(len(days)):
                if days[j] < new_day:
                    next_index = j + 1
            
            
            one_day_pass = costs[0] + dfs(next_index)

            # take a 7 day pass
            new_day = days[i] + 7
            next_index = 0

            for j in range(len(days)):
                if days[j] < new_day:
                    next_index = j + 1
            
            seven_day_pass = costs[1] + dfs(next_index)
            
            # take a 30 day pass
            new_day = days[i] + 30
            next_index = 0

            for j in range(len(days)):
                if days[j] < new_day:
                    next_index = j + 1
            
            thirty_day_pass = costs[2] + dfs(next_index)

            memo[i] = min(one_day_pass, seven_day_pass, thirty_day_pass)
            return memo[i]

        return dfs(0)

        