# 572. Subtree of Another Tree

from typing import Optional
from .utils.tree_node import TreeNode


class SubtreeOfAnotherTree:
    def test_case(self):
        print(__name__)
        root1 = TreeNode(
            3,
            TreeNode(4, TreeNode(1), TreeNode(2)),
            TreeNode(5)
        )
        subRoot1 = TreeNode(4, TreeNode(1), TreeNode(2))
        # self.isSubtree(root1, subRoot1)
        self.model_answer(root1, subRoot1)
        
        root2 = TreeNode(
            3,
            TreeNode(4,
                TreeNode(1), TreeNode(2, TreeNode(0))
            ),
            TreeNode(5)
        )
        subRoot2 = TreeNode(4, TreeNode(1), TreeNode(2))
        # self.isSubtree(root2, subRoot2)
        self.model_answer(root2, subRoot2)

        root3 = TreeNode(1, TreeNode(1))
        subRoot3 = TreeNode(1)
        # self.isSubtree(root3, subRoot3)
        self.model_answer(root3, subRoot3)
        return

    def model_answer(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        if not subRoot: return True
        if not root: return False

        if self.model_answer_same_tree(root, subRoot):
            return True
        
        return (self.model_answer_same_tree(root.left, subRoot) or
                self.model_answer_same_tree(root.right, subRoot))
    
    def model_answer_same_tree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        if not root and not subRoot:
            return True
        
        if root and subRoot and root.val == subRoot.val:
            return (self.model_answer_same_tree(root.left, subRoot.left) and
                    self.model_answer_same_tree(root.right, subRoot.right))
        
        return False


    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        print('----- start -----', root, subRoot)
        result = True
        result = self.search_subnode(root, subRoot)
        print('result', result)
        return result


    def search_subnode(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]):
        print('search_subnode - root.val:', root.val, 'subRoot.val:', subRoot.val)
        if root.val == subRoot.val:
            is_subtree_exist = self.seach_subtree(root, subRoot)
            if is_subtree_exist:
                return True

        if root.left != None:
            is_subtree_exist = self.search_subnode(root.left, subRoot)
            if is_subtree_exist:
                return True
        
        if root.right != None:
            is_subtree_exist = self.search_subnode(root.right, subRoot)
            if is_subtree_exist:
                return True

        return False


    def seach_subtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]):
        if root is None and subRoot is None:
            return True
        elif root is None or subRoot is None:
            return False
        
        print('seach_subtree - root.val:', root.val, 'subRoot.val:', subRoot.val)

        if root.val == subRoot.val:
            left_result = self.seach_subtree(root.left, subRoot.left)
            if left_result:
                return self.seach_subtree(root.right, subRoot.right)
        return False
        