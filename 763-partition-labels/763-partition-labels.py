class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        chidx = []
        mydict = {}
        for index, ch in enumerate(s):
            chidx.append([ch, index])
        for element in chidx:
            if element[0] not in mydict:
                mydict[element[0]] = [element[1]]
            else:
                mydict[element[0]].append(element[1])
        left, right = 0, 0
        max_index = 0
        listslice = [s[left]]
        output = []
        for character in s:
            if right == len(s):
                break
            if character in listslice:
                max_index = max(max_index, max(mydict[character]))
                right = max_index+1
                listslice = s[left:right]
            else:
                output.append(len(listslice))
                max_index = 0
                left = right
                listslice = [s[left]]
                max_index = max(max_index, max(mydict[character]))
                right = max_index+1
                listslice = s[left:right]
        output.append(len(listslice))
        return output
            
            
         
