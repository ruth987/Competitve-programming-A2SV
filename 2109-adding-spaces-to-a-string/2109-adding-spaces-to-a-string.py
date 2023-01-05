class Solution:
    def addSpaces(self, s: str, spaces: List[int]) -> str:
        astring = ""
        spaces_set = set(spaces)
        
        for idx in range(len(s)):
            if idx in spaces_set:
                astring += " "
            astring += s[idx]
            
        return astring
        
            
            