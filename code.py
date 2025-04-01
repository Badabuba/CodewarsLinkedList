class Node():
    def __init__(self, data, next = None):
        self.data = data
        self.next = next

def stringify(node):
    result = ''
    while node != None:
        result += f"{node.data} -> "
        node = node.next
    result += 'None'
    return result