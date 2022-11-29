class Solution:
    def arrangeWords(self, text: str) -> str:
        seen = {}
        output = ""
        text_list = text.split()
        
        for word in text_list:
            n = len(word)
            if n in seen:
                value = seen[n]
                value.append(word.lower())
                seen[n] = value
            else:
                seen[n] = [word]

        for key in sorted(seen):
            output += " ".join(seen[key]) + " "
        return output[:len(output)-1].capitalize()
            
            
        
            