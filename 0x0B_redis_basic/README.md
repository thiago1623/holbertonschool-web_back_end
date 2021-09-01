
## Resources
### Read or watch:
* [Redis commands](https://redis.io/commands)
* [Redis python client](https://redis-py.readthedocs.io/en/stable/)
* [How to Use Redis With Python](https://realpython.com/python-redis/)
* [Redis Crash Course Tutorial](https://www.youtube.com/watch?v=Hbt56gFj998)

### General
* Learn how to use redis for basic operations
* Learn how to use redis as a simple cache

## Requirements
* A ```README.md``` file.
### Install
Install Redis on Ubuntu 18.04
```
$ sudo apt-get -y install redis-server
$ pip3 install redis
$ sed -i "s/bind .*/bind 127.0.0.1/g" /etc/redis/redis.conf
```

## Tasks
* [x] 0. Writing strings to Redis
* [x] 1. Reading from Redis and recovering original type
* [x] 2. Incrementing values
* [x] 3. Storing lists
* [x] 4. Retrieving lists
* [x] 5. Implementing an expiring web cache and tracker
