def findMedianSortedArrays(self, arr1: List[int], arr2: List[int]) -> float:
        x=len(arr1)
        y=len(arr2)
        if x>y:
            return self.findMedianSortedArrays(arr2,arr1)
        low=0
        high=x
        while(low<=high):
            #print(low)
            partitionX=int((low+high)/2)

            partitionY=int(((x+y+1)//2 )-partitionX)
            maxLeftX= float('-inf') if partitionX==0 else arr1[partitionX-1]
            minRightX=float('inf') if partitionX==x else arr1[partitionX]
            maxLeftY = float('-inf') if partitionY == 0 else arr2[partitionY - 1]
            minRightY =  float('inf') if partitionY == y else arr2[partitionY]
            if maxLeftX<=minRightY and maxLeftY<=minRightX:
                if (x+y) %2 ==0:
                    return (max(maxLeftX,maxLeftY) + min(minRightX,minRightY))/2
                else:
                    return max(maxLeftY,maxLeftX)
            elif(maxLeftX>minRightY):
                high=partitionX-1
            else:
                low=partitionX+1