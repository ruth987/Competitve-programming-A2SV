class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        """
        the game is returning the last stone weight left.
        
        [2,7,4,1,8,1]
        what if we sort it so that we can know who to collide with who ?
        
        ohh we choose the heaviest two stones to smash them together.
        so lets sort the array and pick the last two elements then smash it.
        
        [1,1,2,4,7,8]
        i am thinking about using stack. after sorting the arrau in ascending order.
        the brute force approach is as followed: 
        """
        stack = sorted(stones)
        
        while len(stack)>=2:
            s1 = stack.pop()
            s2 = stack.pop()
            if s1!=s2:
                stack.append(abs(s1-s2))
            stack.sort()
        if not stack:
            return 0
        return stack.pop()
        