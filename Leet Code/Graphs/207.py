from collections import defaultdict
class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        dic = defaultdict(list)
        for x in prerequisites:
            dic[x[1]].append(x[0])
        
        # if len(courses) > numCourses:
        #     return False

        visited = set()

        def dfs(course):
            if course not in visited:
                if not dic[course]:
                    return True
                else:
                    visited.add(course)
                    for preq in dic[course]:
                        if not dfs(preq):
                            return False
                    visited.remove(course)
                    dic[course] = []
                    return True
            else:
                return False

        for i in range(numCourses):
            if i not in visited:
                if not dfs(i):
                    return False
        return True