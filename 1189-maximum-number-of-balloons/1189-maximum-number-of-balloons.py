import collections
class Solution:
    def maxNumberOfBalloons(self, text: str) -> int:
        your_dict = collections.Counter(text)
        # balloon {b:1, a:1, l:2, o:2, n:1}
        return int(min(your_dict['b']/1, your_dict['a']/1, your_dict['l']/2, your_dict['o']/2, your_dict['n']/1))
            
