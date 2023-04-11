"""
# Definition for Employee.
class Employee:
    def __init__(self, id: int, importance: int, subordinates: List[int]):
        self.id = id
        self.importance = importance
        self.subordinates = subordinates
"""

class Solution:
    def getImportance(self, employees: List['Employee'], id: int) -> int:
        """
        first: add importance of the root 
        second: add importance of the children
        third : add importance of the children of the children...
        """
        # importance dict
        imp_dict = {}
        # print(employees)
        for emp in employees:
            imp_dict[emp.id] = emp.importance
        
        # parent-child dict
        pc_dict = {}
        for emp in employees:
            pc_dict[emp.id] = emp.subordinates
        total = imp_dict[id]
        def dfs(child):
            nonlocal total
            if not child:
                return
            for num in child:
                total += imp_dict[num]
                dfs(pc_dict[num])
        
        # print(employees[0].subordinates)
        dfs(pc_dict[id])
        return total