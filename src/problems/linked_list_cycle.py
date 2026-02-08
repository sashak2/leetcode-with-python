# 141. Linked List Cycle

from typing import Optional
from .utils.list_node import ListNode

class LinkedListCycle:
    def test_case(self):
        print(__name__)
        case1_list_node = ListNode(3, ListNode(2, ListNode(0, ListNode(-4))))
        self.hasCycle(create_linked_list_cycle(case1_list_node, 1))

        case1_list_node = ListNode(1, ListNode(2))
        self.hasCycle(create_linked_list_cycle(case1_list_node, 0))
        
        case1_list_node = ListNode(1)
        self.hasCycle(create_linked_list_cycle(case1_list_node, -1))
        return

    def hasCycle(self, head: Optional[ListNode]) -> bool:
        print('----- start -----', head)
        result = False
        current_node = head
        node_list = []
        while current_node != None:
            print('current_node.val', current_node.val)
            if current_node in node_list:
                result = True
                break
            node_list.append(current_node)
            current_node = current_node.next
        print('result', result)
        return result
    

def create_linked_list_cycle(list_node, pos):
    print('----- start create_linked_list_cycle -----', pos)
    current_node = list_node
    current_pos = 0
    tailed_node = None
    while pos > -1:
        print('current_node.val', current_node.val)
        if current_pos == pos:
            tailed_node = current_node
        if current_node.next == None:
            current_node.next = tailed_node
            break
        current_node = current_node.next
        current_pos += 1
    return list_node