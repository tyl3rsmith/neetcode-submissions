class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        if endWord not in wordList:
            return 0

        # pattern -> list of words following this pattern
        adj = {}
        wordList.append(beginWord)

        for word in wordList:
            for i in range(len(word)):
                pattern = word[:i] + "*" + word[i + 1:]
            
                if pattern in adj:
                    adj[pattern].append(word)
                else:
                    adj[pattern] = [word]
        
        print(adj)
        # run bfs count levels and flip till we get to the end
        # visit set will mark words we already tried flipping to

        queue = deque([beginWord])
        visited = set()
        visited.add(beginWord)

        res = 1

        while queue:
            for i in range(len(queue)):
                curr_word = queue.popleft()

                if curr_word == endWord:
                    return res

                # generate patterns
                for i in range(len(curr_word)):
                    pattern = curr_word[:i] + "*" + curr_word[i+1:]       

                    for next_word in adj[pattern]:
                 
                        if next_word not in visited:
                            queue.append(next_word)
                            visited.add(next_word)
                    
            res += 1

        return 0           
                            
                            
        
        

            
        