from queue import Queue
from threading import Timer

class Hermes:
    def __init__(self) -> None:
        self.__messages = Queue()
        self.__services = {}

    def put_message(self, service: str, data: dict):
        self.__messages.put([ service, data ])

    def register_service(self, serviceName: str, service) -> None:
        self.__services[serviceName] = service

    def start_work(self) -> None:
        while True:
            message = self.__messages.get()
            if message[0] in self.__services:
                self.__services[message[0]](message[1])
            else:
                pass