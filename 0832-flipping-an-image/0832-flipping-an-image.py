class Solution:
    def flipAndInvertImage(self, image: List[List[int]]) -> List[List[int]]:
        output = []
        for im in image:
            im = im[::-1]
            for idx in range(len(im)):
                if im[idx] == 1:
                    im[idx] = 0
                else:
                    im[idx] = 1
            output.append(im)
        return output
            
            