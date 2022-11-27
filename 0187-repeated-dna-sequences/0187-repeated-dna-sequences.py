class Solution:
    def findRepeatedDnaSequences(self, s: str) -> List[str]:
        left, right = 0, 10
        aset, output = set(), []
        
        
        while right < len(s):
            string = s[left:right]
            if string in aset:
                output.append(string)
            else: # if string not in aset
                aset.add(string)
            left+=1
            right+=1
            
        if s[left:right] in aset:
            output.append(s[left:right])

        return list(set(output))
                
                