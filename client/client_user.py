from __future__ import print_function

import logging

import grpc
import user_pb2 as pb2
import user_pb2_grpc as pb2_grpc

class UserPow(object):
    """
    Cliente gRPC
    """

    def __init__(self):
        self.host = 'localhost'
        self.server_port = 50051

        # Instanciar el channel
        self.channel = grpc.insecure_channel(
            '{}:{}'.format(self.host, self.server_port))

        # vincular el cliente y el servidor
        self.stub = pb2_grpc.UsuarioServicioStub(self.channel)

    def get_url(self, message):
        """
        Cliente2 funcion de llamada a GetUser
        """
        message = pb2.GetUserRequest(name=message)
        print(f'{message}')
        return self.stub.GetUser(message)



if __name__ == '__main__':
    client = UserPow()
    result = client.get_url(message="Soy el cliente 2")
    print(f'{result}')