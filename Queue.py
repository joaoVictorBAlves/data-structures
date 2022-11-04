from abc import ABC, abstractmethod


class EmptyException(Exception):
    pass


class QueueADT(ABC):

    @abstractmethod
    def enqueue(self, elem):
        pass

    @abstractmethod
    def dequeue(self):
        pass

    @abstractmethod
    def first(self):
        pass

    @abstractmethod
    def is_empty(self):
        pass


class Queue(QueueADT):

    def __init__(self):
        self.__data = []

    def enqueue(self, elem):
        self.__data.append(elem)

    def dequeue(self):
        if self.is_empty():
            raise EmptyException
        else:
            self.__data.pop(0)

    def first(self):
        if self.is_empty():
            raise EmptyException
        else:
            return self.__data[0]

    def is_empty(self):
        if len(self.__data) == 0:
            return True
        else:
            return False

    def __str__(self):
        return self.__data.__str__()


if __name__ == "__main__":
    try:
        print("Testes com Fila")
        queue = Queue()
        queue.enqueue("John")
        queue.enqueue("Sarah")
        queue.enqueue("Bill")
        print(queue)
        queue.dequeue()
        print(queue)
        print(queue.first())

    except EmptyException:
        print("Ocorreu um erro: não é possível remover de uma estrutura vazia")