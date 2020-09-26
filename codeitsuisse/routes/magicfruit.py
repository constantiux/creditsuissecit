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
        "maPomegranate": 60,
        "maPineapple": 72,
        "maApple": 60,
        "maRamubutan": 65,
        "maWatermelon": 65,
        "maAvocado": 65
    }
    for fruit, num in data.items():
        logging.info("fruit, num: {}, {}".format(fruit, num))
        result += num * price[fruit]
    return jsonify(result)