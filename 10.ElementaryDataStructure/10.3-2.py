# 節点数 n の2分木を入力とし、O(n)時間でこの木に属する全ての節点のキーをプリントする再帰的手続きを記述せよ。

class Node:
    def __init__(self, key, left=None, right=None):
        self.key = key
        self.left = left
        self.right = right

def print_keys_in_order(node):
    if node is None:
        return
    print_keys_in_order(node.left)   # 左部分木のキーをプリント
    print(node.key)                  # 現在のノードのキーをプリント
    print_keys_in_order(node.right)  # 右部分木のキーをプリント

root = Node(2, 
            Node(1,
                 Node(4, 
                      Node(8), 
                      Node(9)
                      ),
                 Node(5)),
            Node(3,
                 Node(6),
                 Node(7)
                 )
            )
print_keys_in_order(root)

  #         2
  #       /   \
  #      1     3
  #     / \   / \
  #    4   5 6   7
  #   / \
  #  8   9
