class Solution:
    def flipAndInvertImage(self, image: List[List[int]]) -> List[List[int]]:
        output = []
        for im in image:
            inverted = []
            start, end = 0, len(im)-1
            while start < end:
                temp = im[start]
                im[start] = im[end]
                im[end] = temp
                start+=1
                end-=1
            for num in im:
                if num == 1:
                    inverted.append(0)
                else:
                    inverted.append(1)
            output.append(inverted)
        return output
            
            