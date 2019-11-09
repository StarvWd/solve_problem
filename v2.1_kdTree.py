'''
尝试建立KD树
并搜索
'''

class Node:
    def __init__(self):
        self.father = None
        self.left = None
        self.right = None
        self.data = None

    def __str__(self):
        return

    @property
    def brother(self):
        if self.father is None:
            ret = None
        elif self.father.left is self:
            ret = self.father.right
        else:
            ret = self.father.left
        return ret


class KDTree:
    def __init__(self):
        self.root = Node()