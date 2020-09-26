import logging
import json

from flask import request, jsonify

from codeitsuisse import app

logger = logging.getLogger(__name__)

@app.route('/cluster', methods=['POST'])
def evaluateCluster():
    data = request.get_json()
    logging.info("data sent for evaluation {}".format(data))
    ans = Solution()
    result = ans.numIslands(data)
    logging.info("My result :{}".format(result))
    return json.dumps({"answer": result})

class Solution:
    def numIslands(self, grid) -> int:
        if len(grid) == 0: return 0
        rows = len(grid); cols = len(grid[0])
        self.count = sum(grid[i][j] == '1' for i in range(rows) for j in range(cols))
        parent = list(range(rows*cols))
        rank = [0] * rows*cols
        
        def find(x: int) -> int:
            if parent[x] != x:
                parent[x] = find(parent[x])
            return parent[x]
        
        def union(x: int, y: int) -> None:
            xroot = find(x)
            yroot = find(y)
            if xroot == yroot: return 
            if rank[xroot] < rank[yroot]:
                xroot, yroot = yroot, xroot
            parent[yroot] = xroot
            rank[xroot] = max(rank[xroot], rank[yroot]+1)
            self.count -= 1
        
        for i in range(rows):
            for j in range(cols):
                if grid[i][j] == '*':
                    continue
                index = i*cols + j
                if j < cols-1 and grid[i][j+1] == '1':
                    union(index, index+1)
                if i < rows-1 and grid[i+1][j] == '1':
                    union(index, index+cols)
        return self.count