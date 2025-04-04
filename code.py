class Node(object):
    def __init__(self, data=None, next=None):
        self.data = data
        self.next = next

class Context(object):
    def __init__(self, source, dest):
        self.source = source
        self.dest = dest

def reverse(head):
    if head is None or head.next is None:
        return head
    new_head = reverse(head.next)
    head.next.next = head
    head.next = None
    return new_head

def remove_duplicates(head):
    if head is None:
        return
    visited = set()
    visited.add(head.data)
    current = head
    while current.next:
        if current.next.data in visited:
            current.next = current.next.next
        else:
            visited.add(current.next.data)
            current = current.next
    return head

def swap_pairs(head):
    helping_node = Node(next=head)
    prev = helping_node

    while prev.next and prev.next.next:
        first = prev.next
        second = prev.next.next
        prev.next = second
        first.next = second.next
        second.next = first
        prev = first

    return helping_node.next

def sorted_insert(head, data):
    new_node = Node(data)
    if head is None or data < head.data:
        new_node.next = head
        return new_node

    current = head
    while current.next and current.next.data < data:
        current = current.next

    new_node.next = current.next
    current.next = new_node
    return head

def move_node(source, dest):
    if not source:
        raise ValueError
    new_head = source
    source = source.next
    new_head.next = dest
    dest = new_head
    return Context(source, dest)

def stringify(node):
    result = ''
    while node is not None:
        result += f"{node.data} -> "
        node = node.next
    result += 'None'
    return result

def linked_list_from_string(s: str):
    null_values = {"null", "NULL", "nil", "nullptr", "null()", 'None'}
    if s.strip() in null_values:
        return None
    parts = s.split(' -> ')
    values = [int(part) for part in parts if part not in null_values]
    if not values:
        return None
    head = Node(values[0])
    current = head
    for value in values[1:]:
        current.next = Node(value)
        current = current.next
    return head