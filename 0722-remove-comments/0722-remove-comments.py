class Solution:
    def removeComments(self, source: List[str]) -> List[str]:
        answer = []
        inComment = False
        new_string = ""
        
        for line in source:
            if not inComment: 
                new_string = ""
            i, n = 0, len(line)
            
            while i < n:
                if inComment:
                    if line[i:i + 2] == '*/' and i + 1 < n:
                        i += 2
                        inComment = False
                        continue
                    i += 1
                
                else:
                    if line[i:i + 2] == '/*' and i + 1 < n:
                        i += 2
                        inComment = True
                        continue
                    if line[i:i + 2] == '//' and i + 1 < n:
                        break
                    new_string += line[i]
                    i += 1
                    
            if new_string and not inComment:
                answer.append(new_string)
                    
        return answer