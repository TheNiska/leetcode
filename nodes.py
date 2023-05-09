# -*- coding: utf-8 -*-
'''
Нужно добавить аттрибут length и переписать
'''


class Node:
    def __init__(self, val):
        self.val = val
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None

    def get(self, index):
        i = 0
        el = self.head
        if not el:
            return -1
        while i != index and el.next:
            el = el.next
            i += 1
        if i == index:
            return el.val
        else:
            return -1

    def add_at_tail(self, val):
        if self.head:
            el = self.head
            while el.next:
                el = el.next
            el.next = Node(val)
        else:
            self.head = Node(val)

    def add_at_head(self, val):
        node = Node(val)
        node.next = self.head
        self.head = node

    def add_at_index(self, index, val):
        if index == 0:
            self.add_at_head(val)
        elif self.head:
            el = self.head
            i = 0
            while el.next and i < (index - 1):
                el = el.next
                i += 1
            if i == (index - 1):
                node = Node(val)
                node.next = el.next
                el.next = node

    def delete_at_index(self, index):
        if self.head:
            el = self.head
            if index == 0:
                self.head = el.next
                return
            i = 0
            while el.next and i < (index - 1):
                el = el.next
                i += 1
            if i == (index - 1) and el.next:
                el.next = el.next.next

    def show(self):
        el = self.head
        if not el:
            return
        print(f"({el.val})[{0}] --> ", end='')
        i = 0
        while el.next:
            i += 1
            el = el.next
            print(f"({el.val})[{i}] --> ", end='')
        print(f"(None)({i+1})")


lst = LinkedList()
lst.show()

padding = ' ' * 4

while True:
    print('-'*50)
    print("Список команд:")
    print('-'*50)
    print(f"{padding}{'0 - Выход'}")
    print(f"{padding}{'1 - Показать элемент по индексу'}")
    print(f"{padding}{'2 - Добавить в конец'}")
    print(f"{padding}{'3 - Добавить в начало'}")
    print(f"{padding}{'4 - Добавить по индексу'}")
    print(f"{padding}{'5 - Удалить по индексу'}")
    print('-'*50)
    print('Команда: ', end='')
    command = input()

    if command == '0':
        break
    elif command == '1':
        print('Индекс: ', end='')
        index = int(input())
        print(f"Значение по данному индексу: {lst.get(index)}")
    elif command == '2':
        print('Число: ', end='')
        val = int(input())
        lst.add_at_tail(val)
        lst.show()
    elif command == '3':
        print('Число: ', end='')
        val = int(input())
        lst.add_at_head(val)
        lst.show()
    elif command == '4':
        print('Индекс: ', end='')
        index = int(input())
        print('Число: ', end='')
        val = int(input())
        lst.add_at_index(index, val)
        lst.show()
    elif command == '5':
        print('Индекс: ', end='')
        index = int(input())
        lst.delete_at_index(index)
        lst.show()
