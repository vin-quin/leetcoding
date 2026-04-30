// https://leetcode.com/problems/course-schedule/
class Solution {
    public boolean canFinish(int numCourses, int[][] prerequisites) {
        if (prerequisites.length == 0) {
            return true;
        }
        // prereqs are just edges in a directed graph, if we hit a cycle then we have a class dependency conflict and cannot finish
        HashMap<Integer,ArrayList<Integer>> graph = new HashMap<>(); // course: [prereq1,prereq2...]

        for (int[] prereq: prerequisites) {
            if (!graph.containsKey(prereq[0])) {
                graph.put(prereq[0], new ArrayList<Integer>());
            }

            if (!graph.containsKey(prereq[1])) {
                graph.put(prereq[1], new ArrayList<Integer>());
            }
            
            graph.get(prereq[0]).add(prereq[1]);
        }

        int[] status = new int[numCourses]; // 0=unchecked,1=searching,2=no cycle

        for (int i = 0; i < numCourses; i++) {
            if (!dfs(graph, i, status)) return false;
        }

        return true;
    }

    public boolean dfs(HashMap<Integer,ArrayList<Integer>> graph, int course, int[] status) {
        if (status[course] == 1) return false; // cycle
        if (status[course] == 2) return true;  // already safe

        // Go thru every neighbor (prereq) a course needs
        ArrayList<Integer> prereqs = graph.get(course);
        if (prereqs == null) {
            return true;
        }

        status[course] = 1; // mark as visiting
        
        for (int c: prereqs) {
            if (!dfs(graph, c, status)) {
                return false;
            }
        }

        status[course] = 2; // mark as done

        return true;
    }
}