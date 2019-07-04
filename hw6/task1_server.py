import asyncio
import json
import os
storage_path = os.path.join(os.getcwd(), 'data\storage.txt')


# put palm.cpu 10.6 1501864247\n
# ok\n\n
# get test_key\n
# ok\n\n
# get *\n
# ok\npalm.cpu 10.5 1501864247\neardrum.cpu 15.3 1501864259\n\n
# got test_key\n
# error\nwrong command\n\n
class DataProcessing:
    def process_data(self, param):
        temp_list = param.rstrip().split(' ')
        try:
            if temp_list[0] == 'put':
                return self.__process_put(temp_list[1:])
            elif temp_list[0] == 'get':
                return self.__process_get(temp_list[1])
            else:
                raise ServerError
        except ServerError:
            return 'error\nwrong command\n\n'

    def __process_put(self, param):
        with open(storage_path, 'r') as f:
            try:
                data = json.load(f)
            except ValueError:
                data = {}
        if param[0] not in data.keys():
            data[param[0]] = []
        data[param[0]].append((param[1], param[2]))
        data.update(data)
        with open(storage_path, 'w') as f:
            json.dump(data, f)

        return 'ok\n\n'

    def __process_get(self, param):
        resp = 'ok\n'
        with open(storage_path, 'r') as f:
            data = json.loads(f.read())
        if param == '*':
            for key in data.keys():
                for value in data[key]:
                    resp += '{} {} {}\n'.format(key, value[0], value[1])
        else:
            if param in data.keys():
                for value in data[param]:
                    resp += '{} {} {}\n'.format(param, value[0], value[1])

        resp += '\n'
        return resp


class ServerError(Exception):
    pass


class ClientServerProtocol(asyncio.Protocol):
    def connection_made(self, transport):
        self.transport = transport

    def data_received(self, data):
        resp = DataProcessing().process_data(data.decode())
        self.transport.write(resp.encode())


if __name__ == 'main':
    loop = asyncio.get_event_loop()
    coro = loop.create_server(
        ClientServerProtocol,
        '127.0.0.1', 8181
    )

    server = loop.run_until_complete(coro)

    try:
        loop.run_forever()
    except KeyboardInterrupt:
        pass

    server.close()
    loop.run_until_complete(server.wait_closed())
    loop.close()


# print(DataProcessing('put palm.cpu 10.6 1501864247\n').response)
# print(DataProcessing('put palm.cpu 9.6 1501864223\n').response)
# print(DataProcessing('put eardrum.cpu 15.3 1501864259\n').response)
# print(DataProcessing().process_data('get *\n'))
# print(DataProcessing().process_data('get eardrum.cpu\n'))
# print(DataProcessing().process_data('got test_key\n'))
# print(DataProcessing('got test_key\n').response)
