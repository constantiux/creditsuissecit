import logging
import json

from flask import request, jsonify

from codeitsuisse import app

logger = logging.getLogger(__name__)

@app.route('/optimizedportfolio', methods=['POST'])
def evaluatePortfolio():
    data = request.get_json()
    logging.info("data sent for evaluation {}".format(data))
    result = []
    for case in data["inputs"]:
        spotPrice = case["Portfolio"]["SpotPrcVol"]
        portfolioVal = case["Portfolio"]["Value"]
        minimum = optimal = -1
        bestIndex = []
        for index in case["IndexFutures"]:
            optimalHR = index["CoRelationCoefficient"] * (spotPrice) / index["FuturePrcVol"] 
            numFutures = optimalHR * portfolioVal / (index["IndexFuturePrice"] * index["Notional"])
            if minimum == -1:
                minimum = numFutures
                optimal = optimalHR
                bestIndex.append(index["Name"])
            else:
                if numFutures < minimum:
                    minimum = numFutures
                    optimal = optimalHR
                    bestIndex.pop()
                    bestIndex.append(index["Name"])
        optimal = round(optimal, 3)
        minimum = int(round(minimum, 0))
        result.append({"HedgePositionName":bestIndex[0],"OptimalHedgeRatio":optimal, "NumFuturesContract":minimum})
    #inputValue = data.get("input")
    #result = inputValue * inputValue
    #logging.info("My result :{}".format(result))
    #return json.dumps(result)
