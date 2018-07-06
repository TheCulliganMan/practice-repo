from flask import Flask
from flask import render_template
from flask_restful import Api
from flask_restful import Resource
from flask_restful import reqparse
from modals.redis_verbs import HelloRedis
from modals.mongo_verbs import HelloMongo

app = Flask(__name__)
api = Api(app)

# 
# API EXAMPLES IN RESTFUL FLASK
#

### START REDIS API EXAMPLE ###
hello_redis = HelloRedis()
class RedisHelloWorldApi(Resource):
    """ Redis Hello World Example """
    def get(self):
        return hello_redis.get() 
    
    def post(self):
        parser = reqparse.RequestParser(bundle_errors=True)
        parser.add_argument(
            'value', 
            type=str, 
            help='Value to set at key hello in redis', 
            required=True
        )
        args = parser.parse_args()
        hello_redis.post(args["value"])
        return True

    def delete(self):
        return hello_redis.delete()

api.add_resource(
    RedisHelloWorldApi,  # Restful Class 
    '/api/v1/redis/helloworld'  # at path
)
### END REDIS API EXAMPLE ###

### START MONGO API EXAMPLE ###


hello_mongo = HelloMongo()
class MongoHelloWorldApi(Resource):
    """ Mongo Hello World Example """

    def get(self):
        hello_mongo.get()

    def post(self):
        parser = reqparse.RequestParser(bundle_errors=True)
        parser.add_argument(
            'value',
            type=str,
            help='Value to set at key hello in redis',
            required=True
        )
        args = parser.parse_args()
        hello_mongo.post(args["value"])
        return True

    def delete(self):
        return hello_mongo.delete()  # we will just use hello as our key


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
