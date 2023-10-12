class Solution:
    def subStrHash(self, s: str, power: int, modulo: int, k: int, hashValue: int) -> str:
        maps = {chr(i+97):i+1 for i in range(26)}
        arr = [1]
        for i in range(k):
            val = arr[-1] * power 
            arr.append(val)
        hashfind = 0
        for i in range(k):
            hashfind += (arr[i] * (maps[s[i]]))
        l = 0
        r = k
        j = 0
        while r < len(s):
            if hashfind % modulo == hashValue:
                return s[l:r]
            hashfind -= maps[s[l]] * arr[j]
            hashfind //= power
            hashfind += maps[s[r]] * arr[k-1]
            r += 1
            l += 1
        if hashfind%modulo == hashValue:
            return s[l:r]

        return 

"""
class Solution:
    def subStrHash(self, s: str, power: int, modulo: int, k: int, hashValue: int) -> str:
        startval = 0
        for i in range(k):
            startval += (((ord(s[i]) - 96) * (power ** i)))

        def remove_left(ch, val):
            val -= (ord(ch) - 96)
            if val < 0:
                val *= (-1)
            return val
        
        def add_right(ch, val, power):
            val //= power
            val += (((power**(k-1))) * (ord(ch) - 96))

            return val

        # print(startval, "s")
        l, r = 0, k
        while r < len(s):
            # print(s[l:r], startval)
            if hashValue == startval%modulo:
                return s[l:r]

            # print(ord(s[l]) - 96, ord(s[r-1]) - 96)
            # print(startval, s[l:r])
            startval = remove_left(s[l], startval)
            startval = add_right(s[r], startval, power)
            
            l += 1
            r += 1
        
        # print(l, r)
        # print(s[l:r], startval)
        if hashValue == startval%modulo:
            return s[l:]
        


        
"""