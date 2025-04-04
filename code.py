from preloaded import Node

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
