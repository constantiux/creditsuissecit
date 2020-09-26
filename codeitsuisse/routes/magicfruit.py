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
        "maPomegranate": 62,
        "maPineapple": 62,
        "maApple": 62,
        "maRamubutan": 62,
        "maWatermelon": 62,
        "maAvocado": 62
    }
    for fruit, num in data.items():
        logging.info("fruit, num: {}, {}".format(fruit, num))
        result += num * price[fruit]
    return jsonify(result)