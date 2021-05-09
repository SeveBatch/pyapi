import json
import DBService
import flask
from flask import request, jsonify

app = flask.Flask(__name__)
app.config["DEBUG"] = True

@app.route('/', methods=['GET'])
def home():
    return """<h1>Welcome</h1>

    <p>This is a simple API to retrieve statistics about its inputs/outputs</p>
    <h1>Usage</h1>
    <h2>Add Action</h2>
    <p> Accepts a json serialized string of the form below and maintains
        an average time for each action. Mixed return: 200: Success. 400: Failure</p>
    <h2>Statistics</h2>
    <p> Returns a serialized json array of the average time for each action that has
        been provided to the addAction function.Mixed return: 200: Success. 400: Failure</p>
    """

#Finds defined actions and adds a new entry in
#Alternatively we could accept another parameter to add UUIDs to the rows,
#so that this could be a true upsert
@app.route('/action', methods=['PUT'])
def addAction():
    input = request.get_json()

    #Retrieve from our service
    DBService.upsert(input)
    data = DBService.getAll()

    #return outcome of the action upsert and save
    return jsonify(data)

@app.route('/stats', methods=['GET'])
def getStats():
    #Retrieve from our service
    data = DBService.getAverages()

    #return outcome of the action upsert and save
    return jsonify(data)

@app.errorhandler(404)
def page_not_found(e):
    return "<p>Not found</p>", 404