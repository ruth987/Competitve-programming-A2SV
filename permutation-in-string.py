class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:

        def generate_hash(string):
            hash_value = 0 
            for ch in string:
                hash_value += ((ord(ch) - 96) ** 4)
            return hash_value 
        
        def remove_left(ch, hash_value):
            return hash_value - ((ord(ch) - 96) ** 4)

        def add_right(ch, hash_value):
            return hash_value + ((ord(ch) - 96) ** 4) 
        
        left, right = 0, len(s1) - 1
        hashed = generate_hash(s2[: right])
        original = generate_hash(s1)

        # print(original)

        while right < len(s2):
            hashed = add_right(s2[right], hashed)
            right += 1
            if hashed == original:
                # print(s2[left : right], hashed)
                return True
            hashed = remove_left(s2[left], hashed)
            left += 1

        return False