# https://leetcode.com/problems/course-schedule/description/
class Solution:
    def canFinish(self, numCourses: int, prerequisites: list[list[int]]) -> bool:
        '''
        {
         1: [0]
        }
        valid
        {
         1: [0] 
         0: [1]
        }
        invalid
        '''
        
        if len(prerequisites) <= 0:
            return True

        graph = {}

        for info in prerequisites:
            target, prereq = info[0], info[1]

            if target not in graph:
                graph[target] = {prereq}
            else:
                graph[target].add(prereq)
            
        print(graph)

        for k, _ in graph.items():
            r = isRequired(graph,k, k, 0, numCourses)
            print(f'{k=}, {r=}')
            if r:
                return False

        return True

# if course bis requiired to take course a
def isRequired(graph, a, b, depth, maxDepth):
    if a not in graph:
        return False # no prereqs
    edges = graph[a]

    if b in edges:
        return True

    if depth == maxDepth:
        return False
    
    for node in edges:
        r = isRequired(graph, node, b, depth+1, maxDepth)

        if r:
            return r
    
    return False
        
def main():
    s = Solution()
    print(s.canFinish(2, [[1, 0]]))
    # print(s.canFinish(2, [[1, 0], [0,1]]))
    # print(s.canFinish(2, [[0,1],[1,0]]))
    # print(s.canFinish(2, [[1, 0], [1, 2], [0,4], [1,9]]))
    # print(s.canFinish(2, [[1, 1]]))

if __name__ == '__main__':
    main()