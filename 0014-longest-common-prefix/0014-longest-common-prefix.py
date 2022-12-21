class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        """
        strs = ["flow", "flower","flight"]
        
        i refers the internal word index
        idx refers the list index
        """
        answer = ""
        strs = sorted(strs, key = lambda word: len(word))
        print(strs)
        for i in range(len(strs[0])):
            for word in strs:
                if word[i] != strs[0][i]:
                    return answer
            answer += strs[0][i]
        return answer
                    
        
            