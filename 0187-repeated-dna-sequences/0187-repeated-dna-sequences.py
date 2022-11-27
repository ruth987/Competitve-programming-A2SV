class Solution:
    def findRepeatedDnaSequences(self, s: str) -> List[str]:
        """
        letters in the dna sequence are : A C G T
        
        - the substrings in the output list has to be unique.
        - the substrings has to occur more than once.
        
        Input: s = "AAAAACCCCCAAAAACCCCCCAAAAAGGGTTT"
        
        we can use a set then if the substring is already in the set then append the
        substring into the output array if not then add it to the set.
        
        two pointers: left and right ...we store the substring in between in a hashmap
        """
        left, right = 0, 10
        aset = set()
        output = []
        
        while right < len(s):
            string = s[left:right]
            if string in aset:
                output.append(string)
            else: # if string not in aset
                aset.add(string)
            left+=1
            right+=1
        string = s[left:right]
        if string in aset:
            output.append(string)
        else:
            aset.add(string)
        return list(set(output))
                
                