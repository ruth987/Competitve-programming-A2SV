class Solution:
    def garbageCollection(self, garbage: List[str], travel: List[int]) -> int:
        def pop_last_zeros(alist):
            while alist and alist[-1] == 0:
                alist.pop()

        travel = [0]+list(accumulate(travel))

        mydict = {"M":0, "G":0, "P":0}
        m_list = []
        p_list = []
        g_list = []
        for gar in garbage:
            for letter in gar:
                mydict[letter] += 1
            
            m_list.append(mydict["M"])
            p_list.append(mydict["P"])
            g_list.append(mydict["G"])
            mydict = {"M":0, "G":0, "P":0}
            
        answer = 0
        pop_last_zeros(m_list)
        pop_last_zeros(p_list)
        pop_last_zeros(g_list)
        
        if m_list:
            answer += (travel[len(m_list)-1] + sum(m_list))
        if p_list:
            answer += (travel[len(p_list)-1] + sum(p_list))
        if g_list:
            answer += (travel[len(g_list)-1] + sum(g_list))
        
        return answer
        