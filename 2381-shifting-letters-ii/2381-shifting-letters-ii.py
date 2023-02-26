class Solution:
    def shiftingLetters(self, s: str, shifts: List[List[int]]) -> str:
        # save the ascii values of each letters
        
        arr1 = list(s)
        arr2 = [0]*(len(arr1)+1)

        # create an array with zero eleemnts to see the effect of shifting
        for start,end,direction in shifts:
            if direction == 0:
                arr2[start] -= 1
                arr2[end+1] += 1
            else: # direction == 1
                arr2[start] += 1
                arr2[end+1] -= 1
           
        
        # find prefix sum of the shifting array
        arr2 = list(accumulate(arr2))
            
        ans = []
        for idx in range(len(arr2)-1):
            result = (((ord(s[idx])-97)+arr2[idx])%26)+97
            ans.append(chr(result))
            
        return "".join(ans)