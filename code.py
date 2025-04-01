class Node:
    def __init__(self, data, next=None): 
        self.data = data
        self.next = next

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
