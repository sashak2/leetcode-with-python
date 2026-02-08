# 21. Merge Two Sorted Lists

from typing import Optional
from .utils.list_node import ListNode

class MergeTwoSortedLists:
    def test_case(self):
        print(__name__)
        self.mergeTwoLists(ListNode(1, ListNode(2, ListNode(4))), ListNode(1, ListNode(3, ListNode(4))))
        self.mergeTwoLists(ListNode(), ListNode())
        self.mergeTwoLists(ListNode(), ListNode(0))
        return

    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        print('----- start -----', list1, list2)
        merged_list = []
        val1_list = self.convert_listnode_to_list(list1)
        val2_list = self.convert_listnode_to_list(list2)
        print('val1_list', val1_list, 'val2_list', val2_list)
        merged_list = val1_list + val2_list
        merged_list.sort(reverse=True)
        print('merged_list', merged_list)
        result = convert_listnode(merged_list)
        print('result', result)
        return result
    
    
    def convert_listnode_to_list(self, list_node: Optional[ListNode]):
        result = []
        while list_node is not None:
            result.append(list_node.val)
            list_node = list_node.next
        return result
    
    
def convert_listnode(value_list):
    print('value_list', value_list)
    result = None
    if len(value_list) >= 1:
        value = value_list.pop()
        result = ListNode(value, convert_listnode(value_list))
    return result