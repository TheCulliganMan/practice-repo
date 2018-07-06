import os
from apistar import App
from apistar import Route
from apistar import types
from apistar import validators

from modals.mongo_verbs import HelloMongo
from modals.redis_verbs import HelloRedis

BASE_DIR = os.path.dirname(__file__)

TEMPLATE_DIR = os.path.join(BASE_DIR, 'templates')
STATIC_DIR = os.path.join(BASE_DIR, 'static')


def index(app: App, name=None):
    return app.render_template("index.html")


class NoSqlPostValidate(types.Type):
    value = validators.String()


hello_redis = HelloRedis()
hello_mongo = HelloMongo()


def mongo_post(data: NoSqlPostValidate):
    valueobj = NoSqlPostValidate(data)
    hello_redis.post(valueobj.value)


def redis_post(data: NoSqlPostValidate):
    valueobj = NoSqlPostValidate(data)
    hello_redis.post(valueobj.value)


routes = [
    Route('/', 'GET', index),
    Route("/api/v1/redis/helloworld", method="GET", handler=hello_mongo.get),
    Route("/api/v1/redis/helloworld", method="POST", handler=redis_post),
    Route("/api/v1/redis/helloworld", method="DELETE",
          handler=hello_mongo.delete),
    Route("/api/v1/mongo/helloworld", method="GET", handler=hello_mongo.get),
    Route("/api/v1/mongo/helloworld", method="POST", handler=mongo_post),
    Route("/api/v1/mongo/helloworld", method="DELETE", handler=hello_mongo.delete)
]

app = App(routes=routes, template_dir=TEMPLATE_DIR, static_dir=STATIC_DIR)

if __name__ == '__main__':
    app.serve('0.0.0.0', 8000, use_debugger=True)
