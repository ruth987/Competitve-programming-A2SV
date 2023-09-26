class Solution:
    def bestTeamScore(self, scores: List[int], ages: List[int]) -> int:
        """
        what if i first sort the arrays based on the ages.
        what if i try to solve this with a greedy approach.
        when ever both the age and the score increases...i keep going because
        there is no conflict. 
        - when age[i]!=age[i-1] and age[i] < age[i-1]:
            i will ignore or not take the older with a lesser score.
        but greedy doesn't work. because what if i ignore the oldest but because 
        i took the younger with more score, it doesn't alow me to take 
        some others that would have increased my score.
        what if i use a heap?
        instead whenever there is a  conflict i have two choice:
            to take the first or the second
        """
        # memo = {}
        # n = len(scores)
        # age_score = [(ages[i], scores[i]) for i in range(n)]
        # age_score.sort()

        # print(age_score)
        # @cache
        # def dp(idx, previdx):
        #     if idx >= n:
        #         return 0
                
        #     if idx>0 and age_score[idx][0] != age_score[previdx][0] and \
        #     age_score[idx][1] < age_score[previdx][1]:
        #         print("conflict", idx, previdx)
        #         return max(dp(idx+1, idx) + age_score[idx][1] - age_score[previdx][1], \
        #         dp(idx+1, previdx))
            
        #     return dp(idx+1, idx) + age_score[idx][1]
        
        # return dp(0, 0)

        #do it with bottom up approach
        n = len(scores)    
        age_score = [(ages[i], scores[i]) for i in range(n)]
        age_score.sort()   
        dp = [0] * n 
        dp[0] = age_score[0][1]  
        for i in range(1, n):
            dp[i] = age_score[i][1]
            for j in range(i):
                if age_score[j][1] > age_score[i][1]:
                    continue
                dp[i] = max(dp[i], age_score[i][1] + dp[j])
       
        return max(dp)