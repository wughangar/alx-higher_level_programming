#!/usr/bin/python3
"""
question 7: singly linked list
"""


class Node:
    """
    class that defines a node of a singly linked list by data
    """
    def __init__(self, data, next_node=None):
        """
        initializes private instance data and next_node
        """
        self.__data = None
        self.__next_node = None
        self.data = data
        self.next_node = next_node

    @property
    def data(self):
        """
        getter: retrives the data

        Returns:
        int data
        """
        return self.__data

    @data.setter
    def data(self, value):
        """
        setter: sets the data 

        Raises:
        TypeError: if data is not an integer
        """

        if not isinstance(data, int):
            raise TypeError("data must be integer")
        else:
            self.__data = value

    @property
    def next_node(self):
        """
        getter: gets the next_node

       Returns:
       value of the node which is an int
       """
        return self.__next_node

    @next_node.setter
    def next_node(self, value):
        """
        setter: sets the value of the next_node

        Raises:
        TypeError: if node in not None or Node
        """
        if value is not None and not isinstance(value, Node):
            raise TypeError("next_node must be a Node object")
        else:
            self.__next_node = value

class SinglyLinkedList:
    """
    class that defines singly linked lists
    """
    def __init__(self, head):
        """
        initializing private instance head
        """
        self.__head = None

    def sorted_insert(self, value):
        """
        inserts new node correctly in increasing order in the list

        Args:
        value: value to be inserted in the new node
        """
        new_node = Node(value)
