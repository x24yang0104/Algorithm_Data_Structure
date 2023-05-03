"""
Description
Given a undirected graph, a node and a target, return the nearest node to given node which value of it is target, return NULL if you can't find.
There is a mapping store the nodes' values in the given parameters.
It's guaranteed there is only one available solution

Example 1:
Input:
{1,2,3,4#2,1,3#3,1,2#4,1,5#5,4}
[3,4,10,50,50]
1
50
Output:
4
Explanation:
2------3  5
 \     |  | 
  \    |  |
   \   |  |
    \  |  |
      1 --4
Give a node 1, target is 50

there a hash named values which is [3,4,10,50,50], represent:
Value of node 1 is 3
Value of node 2 is 4
Value of node 3 is 10
Value of node 4 is 50
Value of node 5 is 50
Return node 4

Example 2:
Input:
{1,2#2,1}
[0,1]
1
1
Output:
2
"""

public class Solution {
    /*
     * @param graph: a list of Undirected graph node
     * @param values: a hash mapping, <UndirectedGraphNode, (int)value>
     * @param node: an Undirected graph node
     * @param target: An integer
     * @return: a node
     */
    public UndirectedGraphNode searchNode(ArrayList<UndirectedGraphNode> graph,
                                          Map<UndirectedGraphNode, Integer> values,
                                          UndirectedGraphNode node,
                                          int target) {
        Queue<UndirectedGraphNode> queue = new LinkedList<>();
        HashSet<UndirectedGraphNode> set = new HashSet<>();
        queue.offer(node);
        set.add(node);
        while (!queue.isEmpty()){
            UndirectedGraphNode current = queue.poll();
            if (values.get(current) == target) {
                return current;
            }
            
            for (UndirectedGraphNode neighbor : current.neighbors) {
                if (!set.contains(neighbor)) {
                    queue.offer(neighbor);
                    set.add(neighbor);
                }
            }
        }
        
        return null;
    }
}
"""
Time Complexity: O(V + E)
Space complexity: O(V + E)
"""