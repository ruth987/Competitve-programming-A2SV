class Solution:
    def findWinners(self, matches: List[List[int]]) -> List[List[int]]:
        winners = []
        losers = []
        losers_counter = {} 
        
        for match in matches:
            if match[1] in losers_counter:
                losers_counter[match[1]] += 1
            else:
                losers_counter[match[1]] = 1
                
        for match in matches:
            if match[0] not in losers_counter:
                winners.append(match[0])
                
        for key,val in losers_counter.items():
            if val == 1:
                losers.append(key)
            
        return [sorted(list(set(winners))) , sorted(losers)]
        