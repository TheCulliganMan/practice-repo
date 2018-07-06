import requests
import json


def test_redis_set():
    """Test to see if all methods work"""
    url = "http://localhost:93/api/v1/redis/helloworld"
    json.loads(requests.post(url, json={"value": "world"}).text)
    assert json.loads(requests.get(url).text) == "world"
    requests.delete(url).text
    assert json.loads(requests.get(url).text) == ""
