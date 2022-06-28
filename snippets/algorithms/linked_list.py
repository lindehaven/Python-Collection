"""Linked list"""

from random import randint

class ListNode:
    """Node class for singly linked list"""
    def __init__(self, value=None):
        self.value = value
        self.next = None

    def __str__(self):
        """Creates a string representation of the node value"""
        return str(self.value)

    def get_value(self):
        """Gets the node value"""
        return self.value

    def set_value(self, value):
        """Sets the node value"""
        self.value = value


class SinglyLinkedList:
    """Class to handle a singly linked list"""
    def __init__(self):
        self.first = None # Refers to the first node in the list

    def __str__(self):
        """Creates a string representation of the list"""
        string = '['
        node = self.first
        while node:
            string += node.__str__()
            if node.next:
                string += ', '
            node = node.next
        string += ']'
        return string

    def append(self, value):
        """Adds a new node at the list tail"""
        node = ListNode(value)
        if self.first is None:
            self.first = node
        else:
            curr = self.first
            while curr.next:
                curr = curr.next
            curr.next = node

    def delete(self, value):
        """Deletes nodes with given value"""
        prev = None
        curr = self.first
        while curr:
            if curr.get_value() == value:
                if prev:
                    prev.next = curr.next
                else:
                    self.first = curr.next
            prev = curr
            curr = curr.next


def main():
    """Main application"""
    sl_list = SinglyLinkedList()
    for _ in range(5):
        value = randint(1, 9)
        sl_list.append(value)
        sl_list.append(0)
    print("Listan före  :", sl_list)
    sl_list.delete(0)
    print("Listan efter :", sl_list)

if __name__ == '__main__':
    main()
