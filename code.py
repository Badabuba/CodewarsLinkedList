""" For your information:
class Node(object):
    def __init__(self, data):
        self.data = data
        self.next = None
"""
class Node(object):
    def __init__(self, data):
        self.data = data
        self.next = None
def sorted_insert(head, data):
    # Your code goes here.
    # Make sure to return the head of the list.
    if head is None:
        data = Node(data)
        return data
    saved_head = head
    iteration = 1
    while head:
        if head.next is None:
            head.next = Node(data)
            break
        if head.data > data and iteration == 1:
            data = Node(data)
            data.next = head
            return data
        if head.next.data > data:
            temp = head.next
            data = Node(data)
            head.next = data
            data.next = temp
            break
        head = head.next
        iteration += 1
    return saved_head