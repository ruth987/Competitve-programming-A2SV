class Solution:
    def nearestValidPoint(self, x: int, y: int, points: List[List[int]]) -> int:
        """
        i will go through the points in points :
        - then find out whether they are valid or not by compairing their x and y
        - then when ever we find valid calculate their manhattan distance then 
        - pair the manhatten distance with index number in a tuple and save it ia a list
        - sort the list based on manhatan distance 
        - return the first manhatan distance index
        """
        store = []
        for idx in range(len(points)):
            if (points[idx])[0] == x or (points[idx])[1]==y: # then they are valid
                manhatan_distance = (abs((points[idx])[0] - x))+(abs((points[idx])[1]-y))
                store.append((manhatan_distance, idx))
        print(store)
        store = sorted(store, key = lambda item: item[0])
        print(store)
        if store:
            return store[0][1]
        return -1