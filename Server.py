from concurrent import futures
import time

import grpc

from generated import Hello_pb2_grpc, Hello_pb2

_ONE_DAY_IN_SECONDS = 60 * 60 * 24


class Greeter(Hello_pb2_grpc.GreeterServicer):
    def SayHello(self, request, context):
        return Hello_pb2.HelloReply(message='Hello, %s!' % request.name)

    def SayHelloAgain(self, request, context):
        return Hello_pb2.HelloReply(message="muhaa!")
def serve():
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    Hello_pb2_grpc.add_GreeterServicer_to_server(Greeter(), server)
    server.add_insecure_port('[::]:50051')
    server.start()
    try:
        while True:
            time.sleep(_ONE_DAY_IN_SECONDS)
    except KeyboardInterrupt:
        server.stop(0)


if __name__ == '__main__':
    serve()
