#!/usr/bin/python3
"""
class Node
"""


class Node():
    """
    defining a clas Node
    """
    def __init__(self, data, next_node=None):
        """
        initilizing a node
        """
        self.data = data
        self.next_node = next_node

    @property
    def data(self):
        """
        property getter
        """
        return self.__data

    @property
    def next_node(self):
        """
        property getter
        """
        return self.__next_node

    @data.setter
    def data(self, data):
        """
        property setter
        """
        if not isinstance(data, int):
            raise TypeError("data must be an integer")
        self.__data = data

    @next_node.setter
    def next_node(self, value):
        """
        property setter
        """
        if isinstance(value, Node):
            self.__next_node = value
        elif value is None:
            self.__next_node = value
        else:
            raise TypeError("next_node must be a Node object")


class SinglyLinkedList():
    """
    definimg a class Singlylinkedlist
    """
    def __init__(self):
        """
        initilizing an instance
        """
        self.__head = None

    def __str__(self):
        """
        printing out the nodes in the list
        """
        current = self.__head
        my_list = []
        while current is not None:
            my_list.append(str(current.data))
            current = current.next_node
        return ("\n".join(my_list))

    def sorted_insert(self, value):
        """
        insert a node in the respective sorted position
        """
        node = Node(value)
        if self.__head is None:
            self.__head = node
            return
        current = self.__head
        if node.data <= current.data:
            node.next_node = current
            self.__head = node
            return
        while current.next_node is not None:
            if node.data <= current.next_node.data:
                node.next_node = current.next_node
                current.next_node = node
                return
            current = current.next_node
        current.next_node = node
