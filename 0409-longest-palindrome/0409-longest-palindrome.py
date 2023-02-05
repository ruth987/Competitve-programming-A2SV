class Solution:
    def longestPalindrome(self, s: str) -> int:
            adict = collections.Counter(s)
            middle_element = False
            result =0
            for key in adict:

                if adict[key] % 2 != 0:
                    middle_element = True

                result = result + (adict[key] // 2) * 2

            if middle_element == True:

                result = result + 1

            return result
