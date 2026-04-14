class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        q = deque()
        dic = defaultdict(list)
        for x,y in prerequisites:
            dic[x].append(y)

        for i in prerequisites:
            if dic[i[1]] == 0:
                q.append(i[1])
        visitset = set()

        def dfs(course):
            if course in visitset:
                return False
            if dic[course]==[]:
                return True

            visitset.add(course)

            for i in dic[course]:
                if not dfs(i): return False
            
            visitset.remove(course)
            dic[course]=[]
            return True
        
        for course in range(numCourses):
            if not dfs(course): return False
        return True
   

        # completed = set()
        # prereq = {}

        # for x,y in prerequisites:
        #     prereq[x]=y
        
        # for i in prerequisites:
        #     print(i)
        #     if i[1] in completed:
        #         completed.add(i[0])
        #         numCourses-=1
        #     elif not prereq.get(i[1],0):
        #         completed.add(i[1])
        #         numCourses-=1
            


        # return numCourses==0