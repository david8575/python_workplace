# 1. 트리
# 트리는 계층적 구조를 가지는 비선형 자료구조로, 노드(Node)로 구성
# 각 노드는 자식 노드를 가질 수 있으며, 루트 노드부터 시작하여 자식 노드를 연결
# 트리의 대표적인 종류에는 이진 트리, AVL 트리, B-트리
# 2. 특징
# 1) 루트 노드: 트리의 가장 위에 있는 노드
# 2) 자식 노드: 부모 노드에 연결된 노드.
# 3) 잎(리프) 노드: 자식 노드가 없는 노드.
# 4) 이진 트리: 각 노드가 최대 두 개의 자식 노드를 가질 수 있는 트리.

# 3. 노드 
class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

# 4. 이진트리
class BinaryTree:
    def __init__(self):
        self.root = None
        
    def insert(self, value):
        if self.root is None:
            self.root = Node(value)
        else:
            self._insert(self.root, value)
            
    def _insert(self, current_node, value):
        if value < current_node.value:
            if current_node.left is None:
                current_node.left = Node(value)
            else:
                self._insert(current_node.left, value)
        elif value > current_node.value:
            if current_node.right is None:
                current_node.right = Node(value)
            else:
                self._insert(current_node.right, value)
        else:
            print(f"{value} is already in the tree!")
            
    def delete(self, value):
        self.root = self._delete(self.root, value)
        
    def _delete(self, node, value):
        if node is None:
            return node
        if value < node.value:
            node.left = self._delete(node.left, value)
        elif value > node.value:
            node.right = self._delete(node.right, value)
        else:
            if node.left is None and node.right is None:
                return None
            elif node.left is None:
                return node.right
            elif node.right is None:
                return node.left
            else:
                min_larger_node = self._find_min(node.right)
                node.value = min_larger_node.value
                node.right = self._delete(node.right, min_larger_node.value)
        return node
    
    def _find_min(self, node):
        while node.left is not None:
            node = node.left
        return node
    
    def preorder_traversal(self, node):
        if node:
            print(node.value, end=" ")
            self.preorder_traversal(node.left)
            self.preorder_traversal(node.right)
            
    def inorder_traversal(self, node):
        if node:
            self.inorder_traversal(node.left)
            print(node.value, end=" ")
            self.inorder_traversal(node.right)
            
    def postorder_traversal(self, node):
        if node:
            self.postorder_traversal(node.left)
            self.postorder_traversal(node.right)
            print(node.value, end=" ")