import sys
input = sys.stdin.readline

n = int(input().strip())
tree = {}

for _ in range(n):
    parent, left, right = input().split()
    tree[parent] = (left, right)

def preorder(node):
    if node == '.':
        return ''
    left, right = tree[node]
    return node + preorder(left) + preorder(right)

def inorder(node):
    if node == '.':
        return ''
    left, right = tree[node]
    return inorder(left) + node + inorder(right)

def postorder(node):
    if node == '.':
        return ''
    left, right = tree[node]
    return postorder(left) + postorder(right) + node

print(preorder('A'))
print(inorder('A'))
print(postorder('A'))
