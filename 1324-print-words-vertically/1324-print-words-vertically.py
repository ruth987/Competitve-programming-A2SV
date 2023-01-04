class Solution:
    def printVertically(self, s: str) -> List[str]:

        word_list = s.split()
        
        max_len = 1
        for word in word_list:
            if len(word) > max_len:
                max_len = len(word)
                
        answer = []
        
        for idx in range(max_len):
            a = ""
            for word in word_list:
                
                if idx >= len(word):
                    a += " "
                    continue
                    
                a += word[idx]
            a = a.rstrip()
            answer.append(a)
        return answer
            
            