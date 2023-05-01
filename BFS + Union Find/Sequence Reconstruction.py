"""
Description
Check whether the original sequence org can be uniquely reconstructed from the sequences in seqs. The org sequence is a permutation of the integers from 1 to n, with 1≤n≤10^4.
Reconstruction means building a shortest common supersequence of the sequences in seqs (i.e., a shortest sequence so that all sequences in seqs are subsequences of it). Determine whether there is only one sequence that can be reconstructed from seqs and it is the org sequence.
Possible duplicate sequences in seqs

Example 1:
Input:org = [1,2,3], seqs = [[1,2],[1,3]]
Output: false
Explanation:
[1,2,3] is not the only one sequence that can be reconstructed, because [1,3,2] is also a valid sequence that can be reconstructed.

Example 2:
Input: org = [1,2,3], seqs = [[1,2]]
Output: false
Explanation:
The reconstructed sequence can only be [1,2], can't reconstruct the sequence [1,2,3]. 

Example 3:
Input: org = [1,2,3], seqs = [[1,2],[1,3],[2,3]]
Output: true
Explanation:
The sequences [1,2], [1,3], and [2,3] can uniquely reconstruct the original sequence [1,2,3].

Example 4:
Input:org = [4,1,5,2,6,3], seqs = [[5,2,6,3],[4,1,5,2]]
Output:true
"""

"""
Solution: Topological Sort. Check if there is only one item in queue. And finally check if the org == topological sort
"""
class Solution:
    """
    @param org: a permutation of the integers from 1 to n
    @param seqs: a list of sequences
    @return: true if it can be reconstructed only one or false
    """
    def sequence_reconstruction(self, org: List[int], seqs: List[List[int]]) -> bool:
        # write your code here       
        indegree, neighbors = self.get_indegree_and_neighbors(len(org), seqs)[0], self.get_indegree_and_neighbors(len(org), seqs)[1]       
        queue = [x for x in indegree if indegree[x] == 0]
        if len(indegree) != len(org):
            return False;
        result = []       
        while queue:
            if len(queue) > 1:
                return False
            node = queue.pop(0)
            result.append(node)
            for neighbor in neighbors[node]:
                indegree[neighbor] -= 1
                if indegree[neighbor] == 0:
                    queue.append(neighbor)

        return org == result

    def get_indegree_and_neighbors(self, n, seqs):
        indegree = {}
        neighbor = {}
        for seq in seqs:
            for i in range(len(seq)):
                if not indegree.get(seq[i]):
                    indegree[seq[i]] = 0
                if i > 0:
                    indegree[seq[i]] += 1
                if not neighbor.get(seq[i]):
                    neighbor[seq[i]] = []
                if i < len(seq) - 1:
                    neighbor[seq[i]].append(seq[i + 1])
        return indegree, neighbor