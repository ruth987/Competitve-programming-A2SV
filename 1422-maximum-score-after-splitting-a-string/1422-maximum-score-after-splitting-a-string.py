class Solution:
    def maxScore(self, s: str) -> int:

        def countZeros(n):
            ans = 0
            for num in n:
                if num == "0":
                    ans += 1
            return ans
        
        pointer = 1 
        possible_sum = []
        while pointer < len(s):
            #zero in the left
            zeros = countZeros(s[:pointer])
            #ones in the right
            ones = len(s[pointer:])-countZeros(s[pointer:])
            possible_sum.append(zeros+ones)
            pointer+=1
   
        return max(possible_sum)
    