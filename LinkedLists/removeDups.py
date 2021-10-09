# Remove duplicates from an unsorted linked list
# Time Complexity: O(n) - single pass through the linked list
# Space Complexity: O(1) - removal is done in place; no new data structures created

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

def removeDuplicates(list):
    seen = set()
    pointer = list.root
    seen.add(pointer.data)
    while pointer.next is not None:
        if pointer.next.data not in seen:
            seen.add(pointer.next.data)
            pointer = pointer.next
        else:
            temp = pointer.next.next
            pointer.next = temp

def main():
    l = LinkedList(Node(1), 1)
    l.addNode(Node(2))
    l.addNode(Node(3))
    l.addNode(Node(4))
    removeDuplicates(l)
    l.toString()

if __name__ == '__main__':
    main()