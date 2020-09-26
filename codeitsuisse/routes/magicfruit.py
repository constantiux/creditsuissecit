import logging
import json
import ast

from flask import request, jsonify

from codeitsuisse import app

logger = logging.getLogger(__name__)

@app.route('/fruitbasket', methods=['POST'])
def evaluateFruit():
    #data = request.get_json()
    data = request.get_data()
    data = data.decode("UTF-8")
    data = ast.literal_eval(data)
    logging.info("data sent for evaluation {}".format(data))
    result = 0
    price = {
        "maPomegranate": 57,
        "maPineapple": 57,
        "maApple": 57,
        "maRamubutan": 57,
        "maWatermelon": 57,
        "maAvocado": 57
    }
    for fruit, num in data.items():
        logging.info("fruit, num: {}, {}".format(fruit, num))
        result += num * price[fruit]
    return jsonify(result)