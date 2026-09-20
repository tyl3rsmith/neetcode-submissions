class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        visited = [False] * len(strs)
        res = []

        for i in range(len(strs)):
            if not visited[i]:
                group = [strs[i]]
                visited[i] = True
                for j in range(i + 1, len(strs)):
                    if not visited[j] and "".join(sorted(strs[i])) == "".join(sorted(strs[j])):
                        group.append(strs[j])
                        visited[j] = True
                res.append(group)

        return res





        