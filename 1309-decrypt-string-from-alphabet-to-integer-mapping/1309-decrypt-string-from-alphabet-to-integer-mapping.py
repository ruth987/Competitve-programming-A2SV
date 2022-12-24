class Solution:
    def freqAlphabets(self, s: str) -> str:
        # key : value == representer : letter
        mydict = {"1":"a","2":"b","3":"c","4":"d","5":"e","6":"f","7":"g","8":"h",
                  "9":"i","10#":"j","11#":"k","12#":"l","13#":"m","14#":"n",
                  "15#":"o","16#":"p","17#":"q","18#":"r","19#":"s","20#":"t"
                  ,"21#":"u","22#":"v","23#":"w","24#":"x","25#":"y","26#":"z"}
        """
        two pointers : left, right = 0, 2
        conditions : 
        if the last char is hashtag:
            i will look for the the whole s[left: right+1] in mydict
                append that letter to the answer string.
                update both pointers: left += 2 right += 2
        if it isnot:
            i will look for the first integer at the left index in mydict
                append that letter to answer string
                update both pointers by one: left += 1 right += 1
            
        """
        answer = ""
        left, right = 0, 2
        while right < len(s):
            if s[right] == "#":
                answer += mydict[s[left:right+1]]
                left+=3
                right+=3
            else: # if it is a number 
                answer += mydict[s[left]]
                left+=1
                right += 1
        print(left, right)
        while left < len(s):
                answer += mydict[s[left]]
                left +=1
        return answer
                
        