import time
import socket
import logging
from operator import itemgetter


class ClientError(Exception):
    """Raise for wrong input"""


class Client:
    def __init__(self, host, port, timeout=None):
        self.__host = host
        self.__port = port
        self.__timeout = timeout

    def put(self, key, value, timestamp=int((time.time()))):
        with socket.create_connection((self.__host, self.__port)) as sock:
            send_str = 'put {} {} {}\n'.format(key, value, timestamp)
            try:
                sock.sendall(send_str.encode('utf8'))
            except socket.error:
                logging.warning('Unsuccessful sending')
                raise ClientError

    def get(self, key):
        with socket.create_connection((self.__host, self.__port)) as sock:
            send_str = key
            # send_str = 'get {}\n'.format(key)
            try:
                sock.sendall(send_str.encode('utf8'))
            except socket.error:
                logging.warning('Unsuccessful sending')
                raise ClientError
            try:
                data = sock.recv(1024).decode('utf8')
                if data.splitlines()[1:-1] == ['wrong command']:
                    raise ClientError
            except ClientError:
                return data

            new_data = {}
            for d in data.splitlines()[1:-1]:
                temp_list = d.split(' ')
                if temp_list[0] not in new_data.keys():
                    new_data[temp_list[0]] = []
                new_data[temp_list[0]].append(((int(temp_list[2])),
                                               float(temp_list[1])))

            for l in new_data.values():
                l.sort(key=itemgetter(0))
            return new_data


# if __name__ == '__main__':
client = Client('127.0.0.1', 8181, timeout=15)
# client.put('palm.cpu', 0.5, timestamp=1150864247)
# client.put('palm.cpu', 2.0, timestamp=1150864248)
# client.put('palm.cpu', 0.5, timestamp=1150864248)
#
# client.put('eardrum.cpu', 3, timestamp=1150864250)
# client.put('eardrum.cpu', 4, timestamp=1150864251)
# client.put('eardrum.memory', 4200000)

print(client.get('got test_key\n'))
print(client.get('get test_key\n'))
