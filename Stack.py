from abc import ABC, abstractmethod


class EmptyException(Exception):
    pass


class StackADT(ABC):

    @abstractmethod
    def push(self, elem):
        pass

    @abstractmethod
    def pop(self):
        pass

    @abstractmethod
    def top(self):
        pass

    @abstractmethod
    def is_empty(self):
        pass


class Stack(StackADT):

    def __init__(self):
        self.__data = []

    def push(self, elem):
        self.__data.append(elem)

    def pop(self):
        if self.is_empty():
            raise EmptyException
        else:
            self.__data.pop()

    def top(self):
        if self.is_empty():
            raise EmptyException
        else:
            return self.__data[-1]

    def is_empty(self):
        if len(self.__data) == 0:
            return True
        else:
            return False

    def __str__(self):
        return self.__data.__str__()


if __name__ == "__main__":
    try:
        print("Testes com Pilha")
        stack = Stack()
        stack.push("John")
        stack.push("Sarah")
        stack.push("Bill")
        print(stack)
        stack.pop()
        print(stack)
        print(stack.top())

    except EmptyException:
        print("Ocorreu um erro: não é possível remover de uma estrutura vazia")
