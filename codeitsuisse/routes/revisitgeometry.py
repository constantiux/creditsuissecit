import logging
import json

from flask import request, jsonify

from codeitsuisse import app

logger = logging.getLogger(__name__)

@app.route('/revisitgeometry', methods=['POST'])
def evaluateGeometry():
    data = request.get_json()
    logging.info("data sent for evaluation {}".format(data))
    shape, line, xbound, ybound = [[],[],[],[]]
    result = []
    for coord in data["shapeCoordinates"]:
        shape.append((coord["x"], coord["y"]))
        xbound.append(coord["x"])
        ybound.append(coord["y"])
    shape.append(shape[0])  # connecting the last to first point
    xbound.sort()
    ybound.sort()
    xbound[:] = [xbound[0], xbound[-1]]
    ybound[:] = [ybound[0], ybound[-1]] 
    for coord in data["lineCoordinates"]:
        line.append((coord["x"], coord["y"]))
    for i in range(len(shape) - 1):
        ans = intersect(shape[i], shape[i+1], line[0], line[1])
        if ans != -1:
            if ans[0] >= xbound[0] and ans[0] <= xbound[1] and ans[1] >= ybound[0] and ans[1] <= ybound[1]:
                result.append({"x": ans[0], "y": ans[1]})
    #inputValue = data.get("input")
    #result = inputValue * inputValue
    logging.info("My result :{}".format(result))
    return jsonify(result)

def intersect(A,B,C,D):
    try:
        x1, y1 = A[0], A[1]
        x2, y2 = B[0], B[1]
        x3, y3 = C[0], C[1]
        x4, y4 = D[0], D[1]
        px= ( (x1*y2-y1*x2)*(x3-x4)-(x1-x2)*(x3*y4-y3*x4) ) / ( (x1-x2)*(y3-y4)-(y1-y2)*(x3-x4) ) 
        py= ( (x1*y2-y1*x2)*(y3-y4)-(y1-y2)*(x3*y4-y3*x4) ) / ( (x1-x2)*(y3-y4)-(y1-y2)*(x3-x4) )
        return (px, py)
    except:
        return -1