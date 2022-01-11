from dataclasses import dataclass,  field
from sys import _current_frames

@dataclass
class Node:
    """
    Creates a data class for nodes
    Next node can be None so its tail node
    """
    data: int
    next_node: None = field(repr=False, default=None)


@dataclass
class LinkedList:
    """
    Singly linked list
    """
    head: Node = None

    def is_empty(self) -> bool:
        """
        Returns if Linked list is empty or not
        """
        return self.head == None

    def size(self) -> int:
        """
        Returns the number of nodes in the list
        Takes O(n) time
        """
        current = self.head
        count = 0
        while current:
            count += 1
            current = current.next_node
        return count


    def add(self, data):
        """
        Adds a new Node containing data at head of the list
        Takes O(1)
        """
        new_node = Node(data)
        new_node.next_node = self.head
        self.head = new_node


    def search(self, key):
        """
        Search for the first node containing data that matches the key
        Return the node or 'None' if not found
        
        Takes O(n) time
        """
        current = self.head

        while current:
            if current.data == key:
                return current
            else:
                current = current.next_node
        return None


    def __repr__(self) -> str:
        """
        Return a string representation of the list
        Takes O(n) time
        """
        nodes = []
        current = self.head

        while current:
            if current is self.head:
                nodes.append(f"[Head: {current.data}]")
            elif not current.next_node:
                nodes.append(f"[Tail: {current.data}]")
            else:
                nodes.append(f"[{current.data}]")
            
            current = current.next_node
        return '->'.join(nodes)


l = LinkedList()
l.add(1)
l.add(2)
l.add(1)
l.add(5)
l.add(4)
n = l.search(5)
print(n)
