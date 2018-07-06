import redis 

redis = redis.StrictRedis(
    host='redis',  # host is the container name specified in the compose file
    port=6379,  # port has already been set by default in the redis image
    decode_responses=True  # we don't want bytes back
)

class HelloRedis(object):
    def __init__(self):
        pass

    def get(self):
        # we will just use hello as our key
        return redis.get("hello")

    def post(self, value):
        return redis.set("hello", value)

    def delete(self):
        return redis.delete("hello")  # we will just use hello as our key
