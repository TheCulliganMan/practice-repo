import os

from apistar import App, Route, types, validators

from modals.mongo_verbs import HelloMongo
from modals.redis_verbs import HelloRedis

BASE_DIR = os.path.dirname(__file__)

TEMPLATE_DIR = os.path.join(BASE_DIR, 'templates')
STATIC_DIR = os.path.join(BASE_DIR, 'static')


def index(app: App) -> str:
    return app.render_template("index.html")


class NoSqlPostValidate(types.Type):
    value = validators.String()


hello_redis = HelloRedis()
hello_mongo = HelloMongo()


def mongo_post(data: NoSqlPostValidate) -> str:
    valueobj = NoSqlPostValidate(data)
    hello_redis.post(valueobj.value)
    return ""


def redis_post(data: NoSqlPostValidate) -> str:
    valueobj = NoSqlPostValidate(data)
    hello_redis.post(valueobj.value)
    return ""


routes = [
    Route('/', 'GET', index),
    Route("/api/v1/redis/helloworld", method="GET",
          handler=hello_redis.get, name="redis_get"),
    Route("/api/v1/redis/helloworld", method="POST",
          handler=redis_post, name="redis_post"),
    Route("/api/v1/redis/helloworld", method="DELETE",
          handler=hello_redis.delete, name="redis_delete"),
    Route("/api/v1/mongo/helloworld", method="GET",
          handler=hello_mongo.get, name="mongo_get"),
    Route("/api/v1/mongo/helloworld", method="POST",
          handler=mongo_post, name="mongo_post"),
    Route("/api/v1/mongo/helloworld", method="DELETE",
          handler=hello_mongo.delete, name="mongo_delete")
]

app = App(routes=routes, template_dir=TEMPLATE_DIR, static_dir=STATIC_DIR)

if __name__ == '__main__':
    app.serve('0.0.0.0', 8000, use_debugger=True)
