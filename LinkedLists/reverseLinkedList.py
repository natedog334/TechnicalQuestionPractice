# Reverse the nodes of a linked list
# Time Complexity: O(n) single pass through the linked list
# Space Complexity: O(1) - no new structures created or recursive calls

class Node(object):
    def __init__(self, d, n = None):
        self.data = d
        self.next = n

class LinkedList(object):
    def __init__(self, r, s = 0):
        self.root = r
        self.size = s
    def addNode(self, newNode):
        newNode.next = self.root
        self.root = newNode
    def toString(self):
        pointer = self.root
        while pointer is not None:
            print(pointer.data, end=" ")
            pointer = pointer.next

def reverseList(l):
    current = l.root
    prev = None
    while current is not None:
        save = current.next
        current.next = prev
        prev = current
        current = save
    return prev

def main():
    l = LinkedList(Node(1), 1)
    l.addNode(Node(2))
    l.addNode(Node(3))
    l.addNode(Node(4))
    l.addNode(Node(5))
    l = reverseList(l)
    final = LinkedList(l, 5)
    final.toString()

if __name__ == '__main__':
    main()