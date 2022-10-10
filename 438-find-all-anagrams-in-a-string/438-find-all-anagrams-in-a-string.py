class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        # To solve this problem, looping through substrings of s, sorting them each time and comparing to a sorted p will
        # work, but will take too long for some of the test cases. How else can we solve this?
        
        # We can use dictionaries! Store how many of which letters are in p and substrings of s!
        # E.g. 'ac' -> {'a': 1, 'c': 1}
        
        # However, looping through chars of each substring in s and creating a new dict each time takes too long. Darn.
        # What if we could have one dict representing the current substring of s, and only update the changed values
        # as we move the window across?!
        
        # This function returns a dictionary object containing the number of each letter in a string
        # It includes zeros for letters that are not in the string
        #   E.g. 'ac' -> { 'a': 1, 'b': 0, 'c': 1, ... 'z': 0 }
        def create_char_dict(string):
            chars = {}
            for i in range(26):
                chars[chr(ord('a')+i)] = 0

            for char in string:
                chars[char] += 1
            
            return chars
        
        output = []
        window = len(p)
        
        # Let's create our full alphabet dict for p and the first substring of s (which goes from 0 to the length of p)
        p_chars = create_char_dict(p)
        s_chars = create_char_dict(s[0:window])
        if s_chars == p_chars: output.append(0)

        # Now, each loop we move the substring window of s by 1.
        # We update the s_chars dict to remove 1 from the character no longer included in the window, and add one
        # for the new character! This saves us from looping again!
        
        # When we find a match between p_chars and s_chars for some substring, all we need to do is save i to our output
        i = 0
        while i < (len(s) - window):
            s_chars[s[i]] -= 1
            s_chars[s[i + window]] += 1
            i += 1
            if s_chars == p_chars: output.append(i)
            
        return output