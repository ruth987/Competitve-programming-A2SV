class Solution:
    def similarPairs(self, words: List[str]) -> int:
        count = 0
        
        for idx in range(len(words)):
            for i in range(idx+1, len(words)):
                if set(words[idx]) == set(words[i]):
                    count += 1
        
        return count