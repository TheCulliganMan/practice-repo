import requests
import json


def test_redis_set():
    """Test to see if all methods work"""
    url = "http://lin1pr1ap1:94/api/v1/redis/helloworld"
    assert requests.post(url, json={"value": "world"}).text == ''
    assert requests.get(url).text == "world"
    assert requests.delete(url).text == ""
    assert requests.get(url).text == ""

def test_mongo_set():
    """Test to see if all methods work"""
    url = "http://lin1pr1ap1:94/api/v1/mongo/helloworld"
    assert requests.post(url, json={"value": "world"}).text == ''
    assert requests.get(url).text == "world"
    assert requests.delete(url).text == ""
    assert requests.get(url).text == ""
