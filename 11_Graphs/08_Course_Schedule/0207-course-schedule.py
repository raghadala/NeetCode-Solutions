"""
Problem: LeetCode 207 - Course Schedule

Key Idea:
The problem can be reduced to detecting cycles in a directed graph. We can represent the course prerequisites as directed edges between nodes (courses). If there is a cycle in the graph, it means we can't complete all courses.

Time Complexity:
- Constructing the graph takes O(numCourses + len(prerequisites)) time, where numCourses is the number of courses and len(prerequisites) is the number of prerequisites.
- Detecting a cycle in a directed graph takes O(V + E) time, where V is the number of vertices (courses) and E is the number of edges (prerequisites).
- Therefore, the total time complexity is O(numCourses + len(prerequisites)) + O(V + E), which simplifies to O(numCourses + len(prerequisites)).

Space Complexity:
- The space complexity is O(numCourses + len(prerequisites)), where we store the graph using a dictionary and maintain a set for visited nodes.
"""

#if theres a cycle, return false
# each course is a node and an edge is a prerequesite
# key is course and value is list of prereq
class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        pre = defaultdict(list)  #create adjacency list, each course maps to its prereq
        #store graph representation of prerequisites
        for course, p in prerequisites:
            pre[course].append(p)  #add prereq to course
        
        taken = set()

        def dfs(course):
            if not pre[course]:  # no prereqs
                return True
            
            if course in taken:  #revisited node
                return False
            
            else:
                taken.add(course)

            for p in pre[course]:  #iterate through prereqs for course
                if not dfs(p): return False  #if prereqs cant be complete, false
            
            pre[course] = []  #after processing, set to empty and that satisfied
            return True
        
        for course in range(numCourses):
            if not dfs(course):  #if course cant be completed
                return False

        return True
