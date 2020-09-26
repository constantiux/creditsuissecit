import logging
import json

from flask import request, jsonify

from codeitsuisse import app

logger = logging.getLogger(__name__)

@app.route('/salad-spree', methods=['POST'])
def evaluateSaladSpree():
    data = request.get_json()
    logging.info("data sent for evaluation {}".format(data))
    numSalad = data.get("number_of_salads")
    saladStore = data.get("salad_prices_street_map")
    cheapest = 9999999999999999
    for salad in saladStore:
        cheapest = min(cheapest, checksalad(salad, numSalad))
        logging.info("now cheapest :{}".format(cheapest))
    #inputValue = data.get("input");
    #result = inputValue * inputValue
    #logging.info("My result :{}".format(result))
    logging.info("My result :{}".format(cheapest))
    if cheapest == 9999999999999999:
        cheapest = 0
    result = {"result": cheapest}
    return jsonify(result)

def checksalad(prices, demand):
    salad = 9999999999999999
    a = b = -1
    for p in range(len(prices)):
        #print(a, b)
        if prices[p] == 'X' or (p == len(prices) - 1):
            #print("its x")
            if b >= demand:
                #print(prices[a:b])
                salad = min(salad, maxSum(prices[a:a+b], b, demand))
            a = b = -1
        else:
            #print("not x")
            if a == -1:
                a = p
            if b == -1:
                b = 1
            else:
                b += 1
    return salad

def maxSum(arr, n, k): 

    if (n < k): 
        return 0

    res = 0
    for i in range(k): 
        res += int(arr[i]) 

    curr_sum = res 
    for i in range(k, n): 

        curr_sum += int(arr[i]) - int(arr[i-k]) 
        res = max(res, curr_sum) 

    return res
