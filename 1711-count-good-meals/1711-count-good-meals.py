class Solution:
    def countPairs(self, deliciousness: List[int]) -> int:
        """
        x+y = power of two
        y = power of two -x 
        we check if y is in deliciousness for every x as we go through the array
        
        if y is already in mydict: increament with the count.
        
        whatever the case we check all possible difference
        and we count as we go through the array not at once.
        
        """
        if len(deliciousness) < 2:
            return 0
        power_of_two = []
        i = 0
        while i <= 21:
            power_of_two.append(2**i)
            i+=1
        answer = 0   
        counter = {}
        for food_number in deliciousness:
            # we have to check for y = power of two - x
            for pot in power_of_two:
                if pot-food_number in counter:
                    answer += counter[pot-food_number]
            
            if food_number in counter:
                counter[food_number]+=1
            else:
                counter[food_number] =1

        return answer % (10**9 + 7)