class ThroneInheritance:

    def __init__(self, kingName: str): 
        self.kingName = kingName
        self.family = defaultdict(list)
        self.dead = set()

    def birth(self, parentName: str, childName: str) -> None:
        self.family[parentName].append(childName)

    def death(self, name: str) -> None:
        self.dead.add(name)

    def getInheritanceOrder(self) -> List[str]:
        # do dfs
        ans = []
        def dfs(parent):
            if parent not in self.dead:
                ans.append(parent)
             
            for person in self.family[parent]:
                dfs(person)
        dfs(self.kingName)
        return ans


# Your ThroneInheritance object will be instantiated and called as such:
# obj = ThroneInheritance(kingName)
# obj.birth(parentName,childName)
# obj.death(name)
# param_3 = obj.getInheritanceOrder()