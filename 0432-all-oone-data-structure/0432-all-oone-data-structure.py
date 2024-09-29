class ListNode:
    def __init__(self):
        self.keys = set()
        self.prev = None
        self.next = None
        self.count = 0

class AllOne:
    def __init__(self):
        self.key_count = {}  # Dictionary to map keys to their counts
        self.count_list_map = {}  # Dictionary to map counts to list nodes
        self.head = ListNode()  # Dummy head node for doubly linked list
        self.tail = ListNode()  # Dummy tail node for doubly linked list
        self.head.next = self.tail
        self.tail.prev = self.head

    def _remove(self, node: ListNode):
        """Removes the node from the doubly linked list."""
        prev_node = node.prev
        next_node = node.next
        prev_node.next = next_node
        next_node.prev = prev_node
        del self.count_list_map[node.count]

    def _add_new_node_after(self, new_node: ListNode, prev_node: ListNode):
        """Adds new_node after prev_node in the doubly linked list."""
        next_node = prev_node.next
        prev_node.next = new_node
        new_node.prev = prev_node
        new_node.next = next_node
        next_node.prev = new_node
        self.count_list_map[new_node.count] = new_node

    def _move_key(self, key: str, current_count: int, new_count: int):
        """Move the key from the current_count node to the new_count node."""
        current_node = self.count_list_map[current_count]
        current_node.keys.remove(key)

        if new_count not in self.count_list_map:
            new_node = ListNode()
            new_node.count = new_count
            self._add_new_node_after(new_node, current_node if new_count > current_count else current_node.prev)
        
        self.count_list_map[new_count].keys.add(key)

        if not current_node.keys:
            self._remove(current_node)

    def inc(self, key: str) -> None:
        if key in self.key_count:
            current_count = self.key_count[key]
            new_count = current_count + 1
            self.key_count[key] = new_count
            self._move_key(key, current_count, new_count)
        else:
            self.key_count[key] = 1
            if 1 not in self.count_list_map:
                new_node = ListNode()
                new_node.count = 1
                self._add_new_node_after(new_node, self.head)
            self.count_list_map[1].keys.add(key)

    def dec(self, key: str) -> None:
        if key in self.key_count:
            current_count = self.key_count[key]
            new_count = current_count - 1

            if new_count == 0:
                del self.key_count[key]
                self.count_list_map[current_count].keys.remove(key)
                if not self.count_list_map[current_count].keys:
                    self._remove(self.count_list_map[current_count])
            else:
                self.key_count[key] = new_count
                self._move_key(key, current_count, new_count)

    def getMaxKey(self) -> str:
        if self.tail.prev == self.head:
            return ""
        return next(iter(self.tail.prev.keys))

    def getMinKey(self) -> str:
        if self.head.next == self.tail:
            return ""
        return next(iter(self.head.next.keys))