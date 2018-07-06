import redis 

redis = redis.StrictRedis(
    host='redis',  # host is the container name specified in the compose file
    port=6379,  # port has already been set by default in the redis image
    decode_responses=True  # we don't want bytes back
)

class HelloRedis(object):
    def __init__(self):
        pass

    def get(self) -> str:
        # we will just use hello as our key
        resp = redis.get("hello")
        if not resp:
            return ""
        return str(resp)

    def post(self, value) -> str:
        redis.set("hello", value)
        return ""

    def delete(self) -> str:
        redis.delete("hello") 
        return "" # we will just use hello as our key