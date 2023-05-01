"""
Description
Clone an undirected graph. Each node in the graph contains a label and a list of its neighbors. Nodes are labeled uniquely.
You need to return a deep copied graph, which has the same structure as the original graph, and any changes to the new graph will not have any effect on the original graph.
You need return the node with the same label as the input node.

Example1
Input:
{1,2,4#2,1,4#4,1,2}
Output: 
{1,2,4#2,1,4#4,1,2}
Explanation:
1------2  
 \     |  
  \    |  
   \   |  
    \  |  
      4   
Nodes are separated by '#'
1,2,4indicates  a node label = 1, neighbors = [2,4]
2,1,4 indicates a node label = 2, neighbors = [1,4]
4,1,2 indicates a node label = 4, neighbors = [1,2]
"""
class Solution:
    """
    @param node: A undirected graph node
    @return: A undirected graph node
    """
    def clone_graph(self, node: UndirectedGraphNode) -> UndirectedGraphNode:
        # write your code here
        if not node:
            return None
        node_map = self.get_node_map(node)
        self.connect_edge(node_map)
        return node_map[node]
    
    def get_node_map(self, node):
        node_map = {}
        queue = []
        visited = set()
        queue.append(node)
        visited.add(node)
        while queue:
            head = queue.pop(0)
            node_map[head] =  UndirectedGraphNode(head.label)
            for neighbor in head.neighbors:
                if neighbor not in visited:
                    queue.append(neighbor)
                    visited.add(neighbor)
        return node_map
    
    def connect_edge(self, node_map):
        for node, node_clone in node_map.items():
            for neighbor in node.neighbors:
                node_clone.neighbors.append(node_map[neighbor])
"""
Time Complexity: for a graph interation, the time complexity is O(E + V), where E is the number of nodes and V is the number of edges 
Space Complexity: O(E) where E is the number of nodes
"""