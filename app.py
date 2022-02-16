from re import L
from flask import Flask , jsonify, request
import dataanalyst as da


app = Flask(__name__)

# for getting names from GET request 
@app.route("/<string:namevalue>", methods=["GET"])    
def get_names(namevalue):
    data = da.search_engin(da.Name_dataframe("/home/armin/python_project/TestsFiles/nba.csv"),
                             details=False)
    value = data(namevalue)
    return jsonify(value), 200

## for getting details of players in a POST request 

@app.route("/", methods=["POST"])
def get_details():
    get_json = request.get_json() # the json most has a key "name" and "details"
    ## seperate name and details from the json
    for key in get_json.keys():
        if key == "name":
            namevalue = get_json[key]
        elif key == "details": ## details is a list of strings
            details = get_json[key]
    data = da.search_engin(da.Name_dataframe("/home/armin/python_project/TestsFiles/nba.csv"),
                             name=namevalue, details=True)
    value = data(*details)
    return jsonify(value), 200