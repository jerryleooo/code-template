# https://leetcode.com/problems/serialize-and-deserialize-binary-tree/description/

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Codec:

    def serialize(self, root):
        """Encodes a tree to a single string.
        
        :type root: TreeNode
        :rtype: str
        """
        
        def doit(node):
            if node:
                vals.append(str(node.val))
                doit(node.left)
                doit(node.right)
            else:
                vals.append("#")
                
        vals = []
        doit(root)
        return ' '.join(vals)
        

    def deserialize(self, data):
        """Decodes your encoded data to tree.
        
        :type data: str
        :rtype: TreeNode
        """
        
        def doit():
            val = next(vals)
            if val == "#":
                return None
            
            node = TreeNode(int(val))
            node.left = doit()
            node.right = doit()
            
            return node
        
        vals = iter(data.split())
        # 迭代器的使用也是有点意思
        # 不能用 for in 的原因在于
        # 在下一个函数里面，还是得从头遍历 vals
        # 这样是不对的
        return doit()
        

# Your Codec object will be instantiated and called as such:
# codec = Codec()
# codec.deserialize(codec.serialize(root))