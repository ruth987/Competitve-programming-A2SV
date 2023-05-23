class Solution:
    def minimumHammingDistance(self, s: List[int], t: List[int], allowedSwaps: List[List[int]]) -> int:
        parent = {}
        
        def representative(x):
            if x not in parent:
                parent[x] = x
            elif x != parent[x]:
                parent[x] = representative(parent[x])
            return parent[x]

        def union(x, y):
            p_x = representative(x)
            p_y = representative(y)

            if p_x != p_y:
                parent[p_x] = p_y

        for x, y in allowedSwaps:
            union(x, y)

        p_child = defaultdict(list)
        for key, val in parent.items():
            p_child[val].append(key)

        withwho = defaultdict(list)
        for key, val in p_child.items():
            for v in val:
                withwho[v] = val

        taken = set()
        counter = defaultdict(Counter)

        for idx in range(len(s)):
            counter[representative(idx)][s[idx]] += 1

        count = 0
        for i in range(len(s)):
            if counter[representative(i)][t[i]] > 0:
                counter[representative(i)][t[i]] -= 1
            else:
                count += 1

        return count