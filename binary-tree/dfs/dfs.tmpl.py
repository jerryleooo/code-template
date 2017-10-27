# -*- coding: utf-8 -*-

# Template 1: Traverse

class Solution(object):
    def traverse(self, root):
        if not root:
            return

        # do something with root
        traverse(root.left)

        # do something with root
        traverse(root.right)

        # do something with root

# Template 2: Divide & Conquer

class Solution(object):
    def traverse(self, root):
        # null or leaf
        if not root:
            pass
            # Do something and return

        # Divide
        left = self.traverse(root.left)
        right = self.traverse(root.right)

        # Conquer
        result = Merge from left and right
        return result