"""Design your implementation of the linked list. You can choose to use a singly or doubly linked list.
A node in a singly linked list should have two attributes: val and next. val is the value of the current node, and next is a pointer/reference to the next node.
If you want to use the doubly linked list, you will need one more attribute prev to indicate the previous node in the linked list. Assume all nodes in the linked list are 0-indexed.

Implement the MyLinkedList class:

MyLinkedList() Initializes the MyLinkedList object.
int get(int index) Get the value of the indexth node in the linked list. If the index is invalid, return -1.
void addAtHead(int val) Add a node of value val before the first element of the linked list. After the insertion, the new node will be the first node of the linked list.
void addAtTail(int val) Append a node of value val as the last element of the linked list.
void addAtIndex(int index, int val) Add a node of value val before the indexth node in the linked list. If index equals the length of the linked list, the node will be appended to the end of the linked list. If index is greater than the length, the node will not be inserted.
void deleteAtIndex(int index) Delete the indexth node in the linked list, if the index is valid.
 

Example 1:

Input
["MyLinkedList", "addAtHead", "addAtTail", "addAtIndex", "get", "deleteAtIndex", "get"]
[[], [1], [3], [1, 2], [1], [1], [1]]
Output
[null, null, null, null, 2, null, 3]

Explanation
MyLinkedList myLinkedList = new MyLinkedList();
myLinkedList.addAtHead(1);
myLinkedList.addAtTail(3);
myLinkedList.addAtIndex(1, 2);    // linked list becomes 1->2->3
myLinkedList.get(1);              // return 2
myLinkedList.deleteAtIndex(1);    // now the linked list is 1->3
myLinkedList.get(1);              // return 3"""


class ListNode:
    def __init__(self, val):
        self.prev = None
        self.val = val
        self.next = None


class MyLinkedList:

    # def __init__(self):
    #   self.left = ListNode(0)
    #   self.right = ListNode(0)
    #   self.left.next = self.right
    #   self.right.prev = self.left

    # def get(self, index: int) -> int:
    #   cur = self.left.next
    #   while cur and index > 0:
    #     cur = cur.next
    #     index-=1

    #     if cur and cur != self.right and index == 0:
    #       return cur.val
    #     return -1

    # def addAtHead(self, val: int) -> None:
    #    node = ListNode(val)
    #    node.prev = self.left
    #    node.next = self.left.next
    #    self.left.next.prev = node
    #    self.left.next = node

    # def addAtTail(self, val: int) -> None:
    #    node = ListNode(val)
    #    node.prev = self.right.prev
    #    node.next = self.right
    #    self.right.prev.next = node
    #    self.right.prev = node

    # def addAtIndex(self, index: int, val: int) -> None:
    #   cur = self.left.next
    #   while cur and index > 0:
    #     cur = cur.next
    #     index-=1

    #     if cur and index == 0:
    #       node = ListNode(val)
    #       node.prev = cur.prev
    #       node.next = cur
    #       cur.prev.next = node
    #       cur.prev = node

    # def deleteAtIndex(self, index: int) -> None:
    #   cur = self.left.next
    #   while cur and index > 0:
    #       cur = cur.next
    #       index-=1
    #   if cur and cur != self.right and index == 0:
    #       cur.prev.next = cur.next
    #       cur.next.prev = cur.prev
    def __init__(self):
        self.left = ListNode(0)
        self.right = ListNode(0)
        self.left.next = self.right
        self.right.prev = self.left

    def get(self, index: int) -> int:
        cur = self.left.next
        while cur and index > 0:
            cur = cur.next
            index -= 1

        if cur and cur != self.right and index == 0:  # check correct index
            return cur.val
        return -1

    def addAtHead(self, val: int) -> None:
        node, prev, next = ListNode(val), self.left, self.left.next
        node.next, node.prev = next, prev
        next.prev = node
        prev.next = node

    def addAtTail(self, val: int) -> None:
        node, prev, next = ListNode(val), self.right.prev, self.right
        node.next, node.prev = next, prev
        next.prev = node
        prev.next = node

    def addAtIndex(self, index: int, val: int) -> None:
        next = self.left.next
        while next and index > 0:
            next = next.next
            index -= 1

        if next and index == 0:
            node, prev = ListNode(val), next.prev
            node.next, node.prev = next, prev
            next.prev = node
            prev.next = node

    def deleteAtIndex(self, index: int) -> None:
        node = self.left.next
        while node and index > 0:
            node = node.next
            index -= 1

        if node and node != self.right and index == 0:
            node.prev.next = node.next
            node.next.prev = node.prev


# Your MyLinkedList object will be instantiated and called as such:
# obj = MyLinkedList()
# param_1 = obj.get(index)
# obj.addAtHead(val)
# obj.addAtTail(val)
# obj.addAtIndex(index,val)
# obj.deleteAtIndex(index)
