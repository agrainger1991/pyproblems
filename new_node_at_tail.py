class ListNode:
    def __init__(self, value=0, next=None):
        self.value = value  # The valueof the current node
        self.next = next    # Pointer to the next node

def insertNodeAtTail(head, value):
    # Create a new node of value
    new_node = ListNode(value)

    # If the list is empty (head is None) return the new node as the head
    if head is None:
        return new_node

    # Start at the head of the linked list
    current = head

    # Go through list until reaching the last node (node with next == None)
    while current.next is not None:
        current = current.next

    # Set the next pointer of the last node to new node
    current.next = new_node

    # Return the head of the updated linked list
    return head

# Example usage:
head = None
values_to_insert = [3, 5, 7]

for value in values_to_insert:
    head = insertNodeAtTail(head, value)
    # After each insertion, head is updated to point to the head of the list
