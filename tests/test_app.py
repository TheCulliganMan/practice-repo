import requests
import json

def test_redis_set():
    """Test to see if all methods work"""
    url = "http://lin1pr1ap1:93/api/v1/redis/helloworld"
    json.loads(requests.post(url, json={"value": "world"}).text)
    assert json.loads(requests.get(url).text) == "world"
    requests.delete(url).text
    assert json.loads(requests.get(url).text) is None
