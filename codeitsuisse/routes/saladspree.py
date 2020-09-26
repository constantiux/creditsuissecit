import logging
import json

from flask import request, jsonify;

from codeitsuisse import app;

logger = logging.getLogger(__name__)

@app.route('/salad-spree', methods=['POST'])
def evaluateSaladSpree():
    data = request.get_json();
    logging.info("data sent for evaluation {}".format(data))
    numSalad = data.get("number_of_salads")
    saladStore = data.get("salad_prices_street_map")
    cheapest = 999
    for salad in saladStore:
        cheapest = min(cheapest, checksalad(salad, numSalad))
    #inputValue = data.get("input");
    #result = inputValue * inputValue
    #logging.info("My result :{}".format(result))
    logging.info("My result :{}".format(cheapest))
    result = {"result": cheapest}
    return jsonify(result)

def checksalad(prices, demand):
    salad = 999
    flag = temp = 0
    for p in prices:
        logging.info("temp, flag: {}, {}".format(temp, flag))
        if flag == demand:
            salad = min(salad, temp)
            temp = flag = 0
        if p != 'X':
            temp += int(p)
            flag += 1
        elif p == 'X':
            temp = flag = 0
    return salad
