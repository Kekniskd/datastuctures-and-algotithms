from typing import Optional
from dataclasses import dataclass


# Definition for singly-linked list.
@dataclass
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def addToLinkedList(val: int, linkListHead: Optional[ListNode]) -> Optional[ListNode]:
    curr = linkListHead
    while curr is not None:
        if curr.next is None:
            curr.next = ListNode(val)
            break
        curr = curr.next
    return linkListHead


def addTwoNumbers(l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
    curr_l1 = l1
    curr_l2 = l2
    out = ListNode()
    tail = out
    tenz = 0
    while curr_l1 is not None or curr_l2 is not None:
        if curr_l2 is None:
            addition = curr_l1.val + tenz
            tenz = 0
            curr_l1 = curr_l1.next
        elif curr_l1 is None:
            addition = curr_l2.val + tenz
            tenz = 0
            curr_l2 = curr_l2.next
        else:
            addition = curr_l1.val + curr_l2.val + tenz
            tenz = 0
            curr_l1 = curr_l1.next
            curr_l2 = curr_l2.next
        if addition >= 10:
            num_split = [a for a in str(addition)]
            tenz = int(num_split[0])
            tail.next = ListNode(int(num_split[1]))
            tail = tail.next
            # out = addToLinkList(int(num_split[1]), out)
        else:
            tail.next = ListNode(addition)
            tail = tail.next
            # out = addToLinkList(addition, out)
        # if curr_l1 is None and curr_l2 is None:
        #     break

    if tenz > 0:
        tail.next = ListNode(tenz)
    return out.next


Ll1 = ListNode(9, ListNode(9, ListNode(9, ListNode(9, ListNode(9)))))
Ll2 = ListNode(9, ListNode(9, ListNode(9)))
# Ll1 = ListNode(9, ListNode(9))
# Ll2 = ListNode(9)

output = addTwoNumbers(Ll1, Ll2)
curr = output
while curr is not None:
    print(curr.val, end=' -> ')
    curr = curr.next
print('None')
