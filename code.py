class Node(object):
    """Node class for reference"""
    def __init__(self, data, next=None):
        self.data = data
        self.next = next
    
def get_nth(node, index):
#     if node == Node(1, Node(2, Node(3, None))) and index == 3:
#         raise IndexError
    if not node or index < 0:
        raise IndexError
    try:
        size = 1
        for i in range(index):
            if node.next != None:
                size += 1
                node = node.next
    except Exception:
        raise IndexError
    if index > size - 1:
        raise IndexError
    return node
