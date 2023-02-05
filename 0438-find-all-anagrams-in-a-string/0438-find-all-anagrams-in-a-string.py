class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        def create_char_dict(string):
            chars = {}
            for i in range(26):
                chars[chr(ord('a')+i)] = 0

            for char in string:
                chars[char] += 1
            
            return chars
        
        output = []
        window = len(p)

        p_chars = create_char_dict(p)
        s_chars = create_char_dict(s[0:window])
        if s_chars == p_chars: output.append(0)

        i = 0
        while i < (len(s) - window):
            s_chars[s[i]] -= 1
            s_chars[s[i + window]] += 1
            i += 1
            if s_chars == p_chars: output.append(i)
            
        return output
        