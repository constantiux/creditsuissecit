import logging
import json

from flask import request, jsonify
from collections import deque
from codeitsuisse import app

logger = logging.getLogger(__name__)

@app.route('/supermarket', methods=['POST'])
def evaluateSupermarketMaze():
    data = request.get_json()
    logging.info("data sent for evaluation {}".format(data))
    result = {}
    for case, problem in data["tests"].items():
        maze = problem["maze"]
        start = problem["start"]
        end = problem["end"]
        global M, N
        M = len(maze)
        N = len(maze[0])
        solve = BFS(maze, start[1], start[0], end[1], end[0])
        result[case] = solve
    #inputValue = data.get("input")
    #result = inputValue * inputValue
    logging.info("My result :{}".format(result))
    return jsonify({"answers": result})

row = [-1, 0, 0, 1]
col = [0, -1, 1, 0]

def isValid(mat, visited, row, col):
    return (row >= 0) and (row < M) and (col >= 0) and (col < N) \
           and mat[row][col] == 0 and not visited[row][col]

def BFS(mat, i, j, x, y):

    visited = [[False for x in range(N)] for y in range(M)]

    q = deque()
    visited[i][j] = True
    q.append((i, j, 0))
    min_dist = float('inf')

    # loop till queue is empty
    while q:

        # pop front node from queue and process it
        (i, j, dist) = q.popleft()

        # (i, j) represents current cell and dist stores its
        # minimum distance from the source

        # if destination is found, update min_dist and stop
        if i == x and j == y:
            min_dist = dist
            break

        # check for all 4 possible movements from current cell
        # and enqueue each valid movement
        for k in range(4):
            # check if it is possible to go to position
            # (i + row[k], j + col[k]) from current position
            if isValid(mat, visited, i + row[k], j + col[k]):
            # mark next cell as visited and enqueue it
                visited[i + row[k]][j + col[k]] = True
                q.append((i + row[k], j + col[k], dist + 1))

    if min_dist != float('inf'):
        logging.info("The shortest path from source to destination has length {}".format(min_dist))
        return int(min_dist) + 1
    else:
        logging.info("Destination can't be reached from given source")
        return -1