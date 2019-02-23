from pymongo import MongoClient
from pprint import pprint

connection_string = "mongodb://sid:sidleon257@cluster0-shard-00-00-zifyl.mongodb.net:27017,cluster0-shard-00-01-zifyl.mongodb.net:27017,cluster0-shard-00-02-zifyl.mongodb.net:27017/test?ssl=true&replicaSet=Cluster0-shard-0&authSource=admin&retryWrites=true"

client = MongoClient(connection_string)
db = client.admin

serverStatusResult = db.command("serverStatus")
pprint(serverStatusResult)