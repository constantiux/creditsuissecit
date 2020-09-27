import logging
import json

from flask import request, jsonify

from codeitsuisse import app

logger = logging.getLogger(__name__)

@app.route('/contact_trace', methods=['POST'])
def evaluateContactTrace():
    data = request.get_json()
    logging.info("data sent for evaluation {}".format(data))
    result = []
    infectedGene = data["infected"]["genome"]
    for cluster in data["cluster"]:
        if cluster["genome"] == infectedGene:
            temp = data["infected"]["name"] + " -> " + cluster["name"]
            result.append(temp)
        elif cluster["genome"] != infectedGene:
            temp = data["infected"]["name"] + "*" + " -> " + cluster["name"] + " -> " + data["origin"]["name"]
            result.append(temp)
    #inputValue = data.get("input")
    #result = inputValue * inputValue
    logging.info("My result :{}".format(result))
    return jsonify(result)

