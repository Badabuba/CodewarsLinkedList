class Node(object):
    def __init__(self, data=None, next=None):
        self.data = data
        self.next = next

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