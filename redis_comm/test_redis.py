import redis


def test_redis():
    r = redis.Redis(host=host, port=port, password='111111', decode_responses=True)   # host是redis主机，需要redis服务端和客户端都启动 redis默认端口是6379
    pass

if __name__ == '__main__':
    test_redis()
