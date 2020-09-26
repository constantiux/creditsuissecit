import logging
import json

from flask import request, jsonify

from codeitsuisse import app

logger = logging.getLogger(__name__)

@app.route('/fruitbasket', methods=['POST'])
def evaluateFruit():
    data = request.get_json()
    logging.info("data sent for evaluation {}".format(data))
    result = 0
    for fruit, num in data.items():
        logging.info("fruit, num: {}, {}".format(fruit, num))
        result += num * num * 10
    #logging.info("My result :{}".format(cheapest))
    return jsonify(result)