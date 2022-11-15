class Solution:
    def sortSentence(self, s: str) -> str:
        s = s.split()
        s = sorted(s, key = lambda word:word[-1])
        n = len(s)
        answer = ""
        x = 0
        
        for word in s:
            x+=1
            for letter in word: 
                if not letter.isdigit():
                    answer += letter
            if x != n:
                answer += " "
        return answer
        
        