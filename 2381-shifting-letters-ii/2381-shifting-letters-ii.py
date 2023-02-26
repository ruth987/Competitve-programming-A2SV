class Solution:
    def shiftingLetters(self, s: str, shifts: List[List[int]]) -> str:
        # save the ascii values of each letters
        
        arr1 = []
        arr2 = []
        for letter in s:
            arr1.append(ord(letter))
            arr2.append(0)
        arr2 = [0]+arr2
        # create an array with zero eleemnts to see the effect of shifting
        for start,end,direction in shifts:
            if direction == 0:
                arr2[start] -= 1
                arr2[end+1] += 1
            else: # direction == 1
                arr2[start] += 1
                arr2[end+1] -= 1
           
        
        # find prefix sum of the shifting array
        for idx in range(1, len(arr2)):
            arr2[idx] += arr2[idx-1]
            
        # add the ascii array and the second array together
        for idx in range(len(arr1)):
            arr1[idx] += arr2[idx]
            
        # find the element after checking if the ascii value is between 97 and 122
        ans = []
        for val in arr1:
            if val >= 97 and val <= 122:
                ans.append(chr(val))
        # if it is not then substract 26 till you get that
            else:
                while val < 97:
                    val += 26
                while val > 122:
                    val -= 26
                ans.append(chr(val))
                
        return "".join(ans)