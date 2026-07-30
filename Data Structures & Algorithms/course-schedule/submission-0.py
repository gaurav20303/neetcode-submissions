class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        graph = [[] for _ in range(numCourses)]


        visiting = set()
        visited = set()

        for course, prereq in prerequisites:
            graph[prereq].append(course)


        def dfs(course):

            if course in visiting:
                return False

            if course in visited:
                return True

            visiting.add(course)
            for neighbour in graph[course]:
                if not dfs(neighbour):
                    return False

            visiting.remove(course)
            visited.add(course)
            return True



        for i in range(numCourses):
            if not dfs(i):
                return False
        
        return True