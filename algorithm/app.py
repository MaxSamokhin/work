from flask import Flask
from algorithm import get_data
from pymongo import MongoClient

app = Flask(__name__)

MONGO_DB = 'work'
client = MongoClient('127.0.0.1', 27017)
db = client[MONGO_DB]


@app.after_request
def after_request(response):
    response.headers.add('Access-Control-Allow-Origin', '*')
    response.headers.add('Access-Control-Allow-Headers', 'Content-Type,Authorization')
    response.headers.add('Access-Control-Allow-Methods', 'GET,PUT,POST,DELETE,OPTIONS')
    response.headers.add('Content-Type', 'application/json; charset=utf-8')
    return response


@app.route("/data", methods=['GET'])
def main():
    data = get_data(db)
    response = app.response_class(
        response=data,
        status=200,
        mimetype='application/json'
    )
    return response


if __name__ == "__main__":
    app.run('0.0.0.0', 8005)
