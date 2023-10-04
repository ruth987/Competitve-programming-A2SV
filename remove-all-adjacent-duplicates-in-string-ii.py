class Solution:
    def removeDuplicates(self, s: str, k: int) -> str:
        """
        we can use a dictionary to store the count of the letters inside
        a stack and before adding a letter we check if it is similar with
        the last element of the stack, which is the case where we increament
        the count , if it is not we add a new cound. we check the count of
        the top letter if it becomes equal with k then we delete that key from the
        dictionary, we can use a list [letter, count] because one letter can appear
        more than once.
        """
        stack = []

        for idx in range(len(s)):
            if stack and s[idx] == stack[-1][0]:
                stack[-1][1] += 1
                if stack[-1][1] == k:
                    stack.pop()
            else:
                stack.append([s[idx], 1])
        
        return "".join(stack[i][0]*stack[i][1] for i in range(len(stack)))