from abc import ABC, abstractmethod


class ListADT(ABC):

    @abstractmethod
    def get(self, i):
        pass

    @abstractmethod
    def insert(self, i):
        pass

    @abstractmethod
    def remove(self, elem):
        pass

    @abstractmethod
    def removeAt(self, i):
        pass

    @abstractmethod
    def replace(self, i, elem):
        pass

    @abstractmethod
    def size(self):
        pass

    @abstractmethod
    def isEmpty(self):
        pass


class Node:

    def __init__(self, value=None, next=None):
        self.value = value
        self.next = next

    def __str__(self):
        return self.value


class LinkedList(ListADT):

    def __init__(self):
        self.__head = None
        self.__lenght = 0

    def get(self, i):
        i = i % self.__lenght
        if not self.isEmpty():
            pos = 0
            this = self.__head
            while pos <= i:
                if pos == i:
                    return this
                this = this.next
                pos += 1

    def insert(self, elem, i):
        if self.isEmpty():
            self.__head = Node(elem, None)
        else:
            if i <= 0:
                self.__insert_in_the_beginner(elem)
            elif i >= self.__lenght:
                self.__insert_in_the_end(elem)
            else:
                self.__insert_in_the_middle(elem, i)

        self.__lenght += 1

    def remove(self, elem):
        if self.isEmpty():
            raise Exception("Can not remove in a empty list")

        pos = 0
        this = self.__head
        removed = False

        while not removed:
            if this.value == elem:
                self.removeAt(pos)
                removed = True
            else:
                this = this.next
                pos += 1

    def removeAt(self, i):
        if self.isEmpty():
            raise Exception("Can not remove in a empty list")
        if i == 0:
            self.__remove_in_the_beginner()
        elif i == (self.__lenght - 1):
            self.__remove_in_the_end()
        else:
            self.__remove_in_the_middle(i)
        self.__lenght -= 1

    def replace(self, i, elem):
        pos = 0
        this = self.__head
        while pos < self.__lenght:
            if pos != i:
                this = this.next
            else:
                this.value = elem
            pos += 1

    def size(self):
        return self.__lenght

    def isEmpty(self):
        if self.size() == 0:
            return True
        return False

    def __insert_in_the_beginner(self, value):
        aux = self.__head
        self.__head = Node(value, aux)

    def __insert_in_the_end(self, value):
        pos = 0
        this = self.__head
        while pos < self.__lenght:
            if this.next is not None:
                this = this.next
            else:
                this.next = Node(value)
            pos += 1

    def __insert_in_the_middle(self, value, index):
        pos = 0
        this = self.__head
        while pos < index:
            if pos != index - 1:
                this = this.next
            else:
                newNode = Node(value, this.next)
                this.next = newNode
            pos += 1

    def __remove_in_the_beginner(self):
        aux = self.__head.next
        self.__head.next = None
        self.__head = aux

    def __remove_in_the_end(self):
        pos = 0
        this = self.__head
        while pos < self.__lenght - 2:
            if pos != self.__lenght - 2:
                this = this.next
            else:
                this.next = None
            pos += 1

    def __remove_in_the_middle(self, index):
        pos = 0
        this = self.__head
        while pos < index:
            if pos != (index - 1):
                this = this.next
            else:
                prev = this
                deleted = this.next
                prox = deleted.next
                prev.next = prox
                deleted.next = None
            pos += 1

    def __str__(self):
        txt = '[ '
        pos = 0
        this = self.__head
        while pos < self.__lenght:
            txt += str(this.value)
            txt += ' '
            this = this.next
            pos += 1
        txt += ']'

        return txt


if __name__ == '__main__':
    # Tests with the list
    lista = LinkedList()
    print(lista.isEmpty())
    lista.insert("A", 0)
    lista.insert("C",3)
    lista.insert("B",1)
    print(lista)
    print(lista.get(0))
    lista.remove("C")
    print(lista)
    lista.removeAt(0)
    print(lista)
    lista.replace(0,"A")
    print(lista)
