from pymongo import MongoClient

mongo_client = MongoClient(
    'mongod',  # Container name as specified in the compose linkage
    27017  # Default mongo port defined by the mongodb image
)
db = mongo_client.mongo_hello_world_db
db_hello = db.hello

class HelloMongo(object):
    def __init__(self):
        pass

    def get(self):
        # we will just use hello as our key
        result = db_hello.find_one()
        if result and "hello" in result:
            return result["hello"]
        return None

    def post(self, value):
        db_hello.remove()  # upsert
        db_hello.insert_one({"hello": value})
        return True

    def delete(self):
        return db_hello.remove()
