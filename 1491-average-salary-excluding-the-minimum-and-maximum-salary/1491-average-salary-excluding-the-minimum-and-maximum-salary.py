class Solution:
    def average(self, salary: List[int]) -> float:
        max_salary = max(salary)
        min_salary = min(salary)
        
        
        return (sum(salary)-(max_salary+min_salary))/(len(salary)-2)