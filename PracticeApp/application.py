from flask import Flask
from flask import render_template
from flask_restful import Api
from flask_restful import Resource
from flask_restful import reqparse
import redis
from pymongo import MongoClient

app = Flask(__name__)
api = Api(app)

# 
# API EXAMPLES IN RESTFUL FLASK
#

### START REDIS API EXAMPLE ###
redis = redis.StrictRedis(
    host='redis',  # host is the container name specified in the compose file
    port=6379,  # port has already been set by default in the redis image
    decode_responses=True # we don't want bytes back
)
class RedisHelloWorldApi(Resource):
    """ Redis Hello World Example """
    def get(self):
        return redis.get("hello")  # we will just use hello as our key
    
    def post(self):
        parser = reqparse.RequestParser(bundle_errors=True)
        parser.add_argument(
            'value', 
            type=str, 
            help='Value to set at key hello in redis', 
            required=True
        )
        args = parser.parse_args()
        redis.set("hello", args["value"])
        return True

    def delete(self):
        return redis.delete("hello")  # we will just use hello as our key

api.add_resource(
    RedisHelloWorldApi,  # Restful Class 
    '/api/v1/redis/helloworld'  # at path
)
### END REDIS API EXAMPLE ###

### START MONGO API EXAMPLE ###

mongo_client = MongoClient(
    'mongod',  # Container name as specified in the compose linkage
    27017 # Default mongo port defined by the mongodb image
)
db = mongo_client.mongo_hello_world_db
db_hello = db.hello
class MongoHelloWorldApi(Resource):
    """ Mongo Hello World Example """

    def get(self):
        return db_hello.find_one()  # we will just use hello as our key

    def post(self):
        parser = reqparse.RequestParser(bundle_errors=True)
        parser.add_argument(
            'value',
            type=str,
            help='Value to set at key hello in redis',
            required=True
        )
        args = parser.parse_args()
        db_hello.insert_one({"hello": args["value"]})
        return True

    def delete(self):
        return db_hello.remove() # we will just use hello as our key


api.add_resource(
    MongoHelloWorldApi,  # Restful Class
    '/api/v1/mongo/helloworld'  # at path
)
### END MONGO API EXAMPLE ###

### START HTML EXAMPLE ###
@app.route("/", methods=["GET"])
def index():
    return render_template('index.html')
### END HTML EXAMPLE ### 

if __name__ == '__main__':
    app.run(
        host="0.0.0.0",  # expose beyond local host. (need to do this inside a container) 
        port=8000,  # Use port 8000
        debug=True
    )
