class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
        """
        start at image[sr][sc]
        """
        ans = image[::]
        if color == image[sr][sc]:
            return ans
        rows = len(image)
        cols = len(image[0])
        source = image[sr][sc]
        
        def changecolor(r,c):
            if r >= len(image) or r <= -1 or c >= cols or c <= -1:
                return
            if image[r][c] != source:
                return
            ans[r][c] = color
            changecolor(r+1,c)
            changecolor(r-1,c)
            changecolor(r, c+1)
            changecolor(r, c-1)

        changecolor(sr,sc)
        return ans