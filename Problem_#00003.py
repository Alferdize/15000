class Node:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right



def serialize(root):
    if root is None:
        return '#'
    return '{} {} {}'.format(root.val, serialize(root.left), serialize(root.right))

def deserialize(data):
    def helper():
        val = next(vals)
        print(val)
        if val == '#':
            return None
        node = Node(val)
        node.left = helper()
        node.right = helper()
        return node
    vals = iter(data.split())
    return helper()


node = Node('root', Node('left', Node('left.left')), Node('right'))
print(serialize(node))
print(deserialize(serialize(node)))
assert deserialize(serialize(node)).left.left.val == 'left.left'