# 중위 순회 inorder traseval
def inOrder(list_1, list_2, root, n):
    if root <1 or 2**n <= root or list_1[root] != 0:
        return
    inOrder(list_1, list_2, root*2)
    list_1[root] = list_2.pop()
    inOrder(list_1, list_2, root*2+1)