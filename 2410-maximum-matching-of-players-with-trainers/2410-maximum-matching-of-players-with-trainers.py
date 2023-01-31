class Solution:
    def matchPlayersAndTrainers(self, players: List[int], trainers: List[int]) -> int:
        players.sort()
        trainers.sort()
        p_ptr, t_ptr = 0, 0
        pairs = 0
        while p_ptr < len(players) and t_ptr < len(trainers):
            if players[p_ptr] <= trainers[t_ptr]:
                pairs += 1
                p_ptr += 1
                t_ptr += 1
            else:
                t_ptr += 1
        return pairs