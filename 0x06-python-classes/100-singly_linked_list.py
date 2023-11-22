#!/usr/bin/python3
"""Define a class for a singly linked list."""


class Node:
    """Represent a Node singly linked list."""

    def __init__(self, data, next_node=None):
        """Initialize a new Node.

        Args:
        data (int): The data of the ne Node.
        next_node (Node): The next node of the new Node
        """
        self.data = data
        self.next_node = next_node

    @property
    def data(self):
        """Get the current data of the node."""
        return self.__data

    @data.setter
    def data(self, value):
        if not isinstance(value, int):
            raise TypeError("data must be an integer")
        self.__data = value

    @property
    def next_node(self):
        """Return the next node."""
        return self.__next_node

    @next_node.setter
    def next_node(self, value):
        """Set the next node."""
        if value is not None and not isinstance(value, Node):
            raise TypeError("next_node must be a Node object")
        self.__next_node = value


class SinglyLinkedList:
    """Represent a singly linked list."""
    def __init__(self):
        """Initialize a new Node.

        Args:
        data (int): The data of the ne Node.
        next_node (Node): The next node of the new Node
        """
        self.head = None

    def sorted_insert(self, value):
        new_node = Node(value)
        if self.head is None or self.head.data > value:
            new_node.next_node = self.head
            """Get the data of the Singly_linked lists."""
            self.head = new_node
            return

        current = self.head
        while current.next_node is not None and current.next_node.data < value:
            current = current.next_node

        new_node.next_node = current.next_node
        """Set the current node,"""
        current.next_node = new_node

    def __str__(self):
        result = ""
        current = self.head
        while current is not None:
            result += str(current.data) + "\n"
            current = current.next_node
            """Return the next node."""
        return result
