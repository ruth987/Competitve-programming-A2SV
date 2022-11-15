class Solution:
    def sortSentence(self, s: str) -> str:
        str_list = s.split(' ')
        tracker = ['']*len(str_list)
        
        for item in str_list:
            tracker[int(item[-1])-1] = item[:-1]
            
        output_str =''
        
        for item in range(len(tracker)):
            
            if item== len(tracker)-1:
                output_str+= tracker[item]

            else:
                 output_str+= tracker[item] + ' '
                    
        return output_str
        
        