class Solution:
    def findWinners(self, matches: List[List[int]]) -> List[List[int]]:
        winners = [match[0] for match in matches]
        losers = [match[1] for match in matches]
        perfect_winners = list(set(winners) - set(losers))
        loser_counter = collections.Counter(losers)
        one_lost = []
        for loser in loser_counter:
            if loser_counter[loser] == 1:
                one_lost.append(loser)
        return [sorted(perfect_winners), sorted(one_lost)]