import logging
import json

from flask import request, jsonify

from codeitsuisse import app

logger = logging.getLogger(__name__)

@app.route('/clean_floor', methods=['POST'])
def evaluateCleanFloor():
    data = request.get_json()
    logging.info("data sent for evaluation {}".format(data))
    tests = data.get("tests")
    result = {}
    for case, floor in tests.items():
        logging.info("floor is {}".format(floor))
        count = check(floor["floor"])
        result[case] = count
    logging.info("My result :{}".format(result))
    return jsonify({"answers": result})

def check(floor):
    flag = 1
    total = 0
    if floor[0] == 1:
        total += 1
    while True:
        if len(floor) == 1:
            break
        if flag == 1:
            stop = len(floor) - 1
            while True:
                if floor[stop] != flag:
                    stop -= 1
                else:
                    floor[stop] ^= 1
                    stop += 1
                    break
            floor[:] = floor[1:stop]
            total += len(floor)
            print(floor)
            print(total)
            flag ^= 1
        elif flag == 0:
            stop = 0
            while True:
                if floor[stop] != flag:
                    stop += 1
                else:
                    floor[stop] ^= 1
                    break
            floor[:] = floor[stop:-1]
            total += len(floor)
            print(floor)
            print(total)
            flag ^= 1
    return total