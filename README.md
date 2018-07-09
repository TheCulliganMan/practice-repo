# practice-repo

Multiple web servers in python

## To start

The following command will pull and build the docker files described in the docker-compose.yml

```bash
docker-compose build
```

Now we want to start the app.

```bash
docker-compose up -d  # d is for daemon
```

Now the app should be running with its' copies of mongodb and redis. (this  can be shortened to `docker-compose up --build -d`)

It is probably about time to check the logs of the application.  We can do this by typing:

```bash
docker-compose logs -f  # f is for follow
```

## Without docker compose

You can acheive the same end without using docker-compose.  I don't know why you would.  The code below should be roughly what you would need to do, in this case you will need to change the linkage of the containers to localhost:port instead of redis:port and mongo:port.

```bash
cd PracticeApp
docker build -t practiceapp .
docker run -name mongo -d -p 27017:27017 mongo:latest
docker run -name redis -d -p 6379:6379 redis:latest
docker run -name practiceapp -p 93:8000 -d practiceapp
```


## General Notes

### Tools

#### PyTest

* if anybody asks you use the hell out of this.
* Tests should probably be in pytest with coverage enabled.  
* https://docs.pytest.org/en/latest/

#### Jupyter / Jupyter Lab

* if you haven't used these check them out this week. `pip install jupyter`
* super cool repl for python
* web based and allows exposed kernels to a web browser
* inline visualization
* markdown support!!!
* R / Haskel / Scala Support
* just super cool.

#### Requests

* use this to call apis
* `pip install requests`
* http://docs.python-requests.org/en/master/

### Rest Servers

#### Flask

* great general purpose framework
* the best to develop quickly in
* tons of extensions
* mid / fast

#### Flask-Restful

* flask plugin for rest
* slow, but has a good structure.
* uses http verbs to define classes(PUT POST GET DELETE, ETC)

#### Falcon

* You manage everything by hand
* not as many extensions
* fast. 20x the speed (reqs per second) of flask
* runs great on pypy!

#### ApiStar

* kinda strange syntax
* fast, not as fast as falcon but fast.
* self documenting!!!!

    * automatically creates a /docs/ endpoint that shows how to call the api in javascript and python


### Redis

* https://www.credera.com/blog/technology-insights/java/redis-explained-5-minutes-less/
* https://github.com/andymccurdy/redis-py
* in-memory data structure store
* used as a database, cache and message broker
* various data structures:

    * strings
    * hashes
    * lists
    * sets
    * sorted sets with range queries
    * bitmaps
    * hyperloglogs
    * geospatial indexes with radius queries

* LRU (least recently used) eviction
* Key expiry times
* Extremely Fast Single Worker model
* best used when you want something like a python dictionary that spans a network.

### MongoDB

* links:

    * https://www.mongodb.com/what-is-mongodb
    * https://api.mongodb.com/python/current/

* Traditional (ACID) NoSQL
* Use it when you have large data that needs to get sharded over a cluster 
* Has georadius, sharding, and an "Object Store" called GridFS
* Gridfs shards into 256 kb chunks and allows for distributed file storage.

