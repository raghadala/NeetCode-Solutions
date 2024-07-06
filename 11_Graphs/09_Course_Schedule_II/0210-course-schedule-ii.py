"""
Problem: LeetCode 210 - Course Schedule II

Key Idea:
This problem is an extension of the previous Course Schedule problem (LeetCode 207). We need to return the order in which courses can be taken. We can use the topological sorting approach to solve this.

Time Complexity:
- Constructing the graph takes O(numCourses + len(prerequisites)) time, where numCourses is the number of courses and len(prerequisites) is the number of prerequisites.
- Performing topological sorting using BFS takes O(V + E) time, where V is the number of vertices (courses) and E is the number of edges (prerequisites).
- Therefore, the total time complexity is O(numCourses + len(prerequisites)) + O(V + E), which simplifies to O(numCourses + len(prerequisites)).

Space Complexity:
- The space complexity is O(numCourses + len(prerequisites)), where we store the graph using a dictionary, maintain a list for in-degrees, and use a queue for BFS traversal.
"""


class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        preReq = defaultdict(list)
        #build graph
        for course,p in prerequisites:
            preReq[course].append(p)
        
        res = []
        visited, cycle = set(), set()

        def dfs(course):
            # terminating case
            if course in cycle:
                return False
            
            if course in visited:
                return True
            else:
                cycle.add(course)
            
            for p in preReq[c]:
                if not dfs(p):
                    return False
            cycle.remove(course). #after processing add to visited
            visited.add(course)
            res.append(course)
            return True

        for c in range(numCourses):
            if dfs(c) == False:
                return []
            
        return res
