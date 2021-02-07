



class Client():
    def __init__(self, service_client, host, port):
        reactor.connectTCP(cfg.SERVER_HOST, cfg.SERVER_PORT,
                           ClientProtocolFactory(service_client))

    def run(self):
        reactor.run()

    def stop(self):
        reactor.callFromThread(reactor.stop)
