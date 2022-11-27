class Solution:
    def findRepeatedDnaSequences(self, s: str) -> List[str]:
        left, right = 0, 10
        aset, output = set(), []
        
        
        for right in range(10, len(s)):
            string = s[left:right]
            if string in aset:
                output.append(string)
            else: # if string not in aset
                aset.add(string)
            left+=1
            
        if s[left:right+1] in aset:
            output.append(s[left:right+1])

        return list(set(output))
                
                