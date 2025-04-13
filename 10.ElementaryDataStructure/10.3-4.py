# 節点数 n の任意の木を入力とし、O(n)時間でこの木に属する全ての節点のキーをプリントする非再帰的手続きを記述せよ。圃場データ構造としてスタックを使え。
# ただし、木は、左-子、右-兄弟表現を用いて格納されている。
#       2
#      / \
#     1   3
#    / \  / \
#   4   5 6  7
#  / \
# 8   9

class Node:
    def __init__(self, key, first_child=None, next_sibling=None):
        self.key = key
        self.first_child = first_child
        self.next_sibling = next_sibling

def print_tree_non_recursive(root):
    if root is None:
        return

    stack = [root]
    while stack:
        node = stack.pop()
        print(node.key)

        # 兄弟を先に push（後に処理）
        if node.next_sibling:
            stack.append(node.next_sibling)

        # 子を後に push（先に処理）
        if node.first_child:
            stack.append(node.first_child)

# 構築する木:
#       2
#      / \
#     1   3
#    / \  / \
#   4   5 6  7
#  / \
# 8   9

n8 = Node(8)
n9 = Node(9)
n4 = Node(4, n8)
n8.next_sibling = n9

n5 = Node(5)
n4.next_sibling = n5

n1 = Node(1, n4)

n6 = Node(6)
n7 = Node(7)
n6.next_sibling = n7
n3 = Node(3, n6)

n1.next_sibling = n3
root = Node(2, n1)

print_tree_non_recursive(root)
