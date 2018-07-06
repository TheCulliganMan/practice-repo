import json
from wsgiref import simple_server

import falcon

from modals.mongo_verbs import HelloMongo
from modals.redis_verbs import HelloRedis

app = falcon.API()

with open("./templates/index.html") as input_handle:
    INDEX_HTML = input_handle.read()

hello_redis = HelloRedis()
hello_mongo = HelloMongo()


class RenderIndex(object):

    def on_get(self, req, resp):
        resp.content_type = "text/html"
        resp.body = INDEX_HTML


class RenderRedis(object):
    def on_get(self, req, resp):
        resp.status = falcon.HTTP_200
        resp.body = hello_redis.get()

    def on_post(self, req, resp):
        error = False
        try:
            data = json.loads(req.stream.read().decode('utf-8'))
        except Exception:
            resp.body = str(error)
            resp.status = falcon.HTTP_400
            error = True
        if not error:
            if "value" not in data:
                resp.body = str(error)
                resp.status = falcon.HTTP_400
                error = True
            else:
                hello_redis.post(data["value"])
                resp.status = falcon.HTTP_200
                resp.body = ""

    def on_delete(self, req, resp):
        resp.status = falcon.HTTP_200
        resp.body = hello_redis.delete()


class RenderMongo(object):
    def on_get(self, req, resp):
        resp.status = falcon.HTTP_200
        resp.body = hello_redis.get()

    def on_post(self, req, resp):
        error = False
        try:
            data = json.loads(req.stream.read().decode('utf-8'))
        except Exception:
            resp.body = str(error)
            resp.status = falcon.HTTP_400
            error = True
        if not error:
            if "value" not in data:
                resp.body = str(error)
                resp.status = falcon.HTTP_400
                error = True
            else:
                hello_mongo.post(data["value"])
                resp.status = falcon.HTTP_200
                resp.body = ""

    def on_delete(self, req, resp):
        resp.status = falcon.HTTP_200
        resp.body = hello_redis.delete()


render_index = RenderIndex()
render_redis = RenderRedis()
render_mongo = RenderMongo()

app.add_route("/", render_index)
app.add_route("/api/v1/redis/helloworld", render_redis)
app.add_route("/api/v1/mongo/helloworld", render_mongo)

if __name__ == "__main__":
    httpd = simple_server.make_server("0.0.0.0", 8000, app)
    httpd.serve_forever()
