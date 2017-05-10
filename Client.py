"""The Python implementation of the GRPC helloworld.Greeter client."""

from __future__ import print_function

import grpc

from generated import Hello_pb2_grpc, Hello_pb2


def run():
    channel = grpc.insecure_channel('localhost:50051')
    stub = Hello_pb2_grpc.GreeterStub(channel)
    response = stub.SayHello(Hello_pb2.HelloRequest(name='you'))
    response2 = stub.SayHelloAgain(Hello_pb2.HelloRequest(name="Adhav"))

    print("Greeter client received: " + response.message)
    print("Second Client: " + response2.message)


if __name__ == '__main__':
    run()
