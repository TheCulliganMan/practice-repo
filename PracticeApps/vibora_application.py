from vibora import Vibora, Request

from vibora.schemas import Schema, fields

from vibora.responses import Response, JsonResponse

from modals.mongo_verbs import HelloMongo
from modals.redis_verbs import HelloRedis

hello_redis = HelloRedis()
hello_mongo = HelloMongo()

app = Vibora()

with open("templates/index.html", "rb") as input_handle:
    INDEX_HTML = input_handle.read()


class AddValueSchema(Schema):
    # Custom validations can be done by passing a list of functions
    # to the validators keyword param.
    value: str = fields.String()


@app.route('/')
async def home():
    return Response(INDEX_HTML)


@app.route('/api/v1/mongo/helloworld')
async def mongo_hello_world(request: Request):
    if request.method == b"GET":
        return JsonResponse(hello_mongo.get())
    if request.method == b"POST":
        schema = await AddValueSchema.load_json(request)
        hello_mongo.post(schema.value)
        return JsonResponse("")
    if request.method == b"DELETE":
        hello_mongo.delete()
        return JsonResponse("")


@app.route('/api/v1/redis/helloworld', methods=["GET", "POST", "DELETE"])
async def redis_hello_world(request: Request):
    if request.method == b"GET":
        return JsonResponse(hello_redis.get())
    if request.method == b"POST":
        schema = await AddValueSchema.load_json(request)
        hello_redis.post(schema.value)
        return JsonResponse("")
    if request.method == b"DELETE":
        hello_redis.delete()
        return JsonResponse("")


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=8000)
