from flask import Flask, jsonify
from pymongo import MongoClient

app = Flask(__name__)

client = MongoClient()
db = client.test #mi base de datos se llama test
users = db.users #dentro de test, una coleccion es users
tweets = db.tweets #dentro de test, otra coleccion es tweets



@app.route("/")
def hello():
    return "Hello World!"



@app.route("/users/<uid>")
def find_users(uid=None):
	pass


@app.route("/tweets/<mid>")
def find_tweets(mid=None):
	pass

@app.route("/msg")
def find_tweets_by_user():
	pass



if __name__ == '__main__':
	app.run(port=2000)