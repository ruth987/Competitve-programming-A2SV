class Solution:
    def arrangeWords(self, text: str) -> str:
        text = list(text.split())
        alist = []
        
        for word in text:
            alist.append((word.lower(), len(word)))
        
        alist = sorted(alist, key = lambda word:word[1])
        answer = ""
        
        for each in alist:
            answer = answer+" "+each[0]
        
        answer = answer.replace(answer[1], answer[1].upper(),1)
        return answer[1:]
        
            
            
        
            