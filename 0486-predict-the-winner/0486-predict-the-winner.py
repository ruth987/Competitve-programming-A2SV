class Solution:
    def PredictTheWinner(self, nums: List[int]) -> bool:
        """
        turn is true at fist
        if it is false then it is player 2's turn
        
        """
        
        def predictor(start,end,turn): 
            
            if start == end:
                if turn:
                    return [nums[start],0]
                else:
                    return [0, nums[start]]
                
            if turn: # for player one
                score = predictor(start+1, end, False)
                #first poss : take the start
                score[0] += nums[start]
                # first1 = predictor(start+1, end, False)
                # second poss : take from end
                score2= predictor(start, end-1, False)
                score2[0] += nums[end]
                
                if score[0] >= score2[0]:
                    return score
                return score2
                # p1score += max(score[0] ,score2[0])
                # return [score[0], score2[0]]
                
            else: # for player two
                score = predictor(start+1, end, True)
                #first poss : take the start
                score[1] += nums[start]
                # first1 = predictor(start+1, end, False)
                # second poss : take from end
                score2= predictor(start, end-1, True)
                score2[1] += nums[end]
                
                if score[1] >= score2[1]:
                    return score
                return score2
#                 # first poss : take from start
#                 p1_p2score += nums[start]
#                 first2 = predictor(start+1, end, True)
#                 # second poss : take from end
#                 p2_p2score += nums[end]
#                 second2 = predictor(start, end-1, True)
                
#                 p2score += max(first2[1] ,second2[1])
#                 return [p1score, p2score]
        
        ans = predictor(0, len(nums)-1, True)
        # print(ans)
        return ans[0] >= ans[1]
        
        