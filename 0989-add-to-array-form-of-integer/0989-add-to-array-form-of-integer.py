class Solution:
    def addToArrayForm(self, num: List[int], k: int) -> List[int]:
        output = []
        number = int("".join(list(map(str, num))))
        
        for digit in str(number+k):
            output.append(digit)
            
        return output
        