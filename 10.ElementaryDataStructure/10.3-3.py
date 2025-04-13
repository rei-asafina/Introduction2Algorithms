# 節点数 n の2分木を入力とし、O(n)時間でこの木に属する全ての節点のキーをプリントする非再帰的手続きを記述せよ。圃場データ構造としてスタックを使え。

#       2
#      / \
#     1   3
#    / \  / \
#   4   5 6  7
#  / \
# 8   9

def print_keys_in_order_iterative(root):
    stack = []
    current = root

    while stack or current:
        while current:
            stack.append(current)
            current = current.left

        # print("Stack List", " -> ".join(str(node.key) for node in reversed(stack)))
        # Stack List 8 -> 4 -> 1 -> 2
        # Stack List 4 -> 1 -> 2
        # Stack List 9 -> 1 -> 2
        # Stack List 1 -> 2
        # Stack List 5 -> 2
        # Stack List 2
        # Stack List 6 -> 3
        # Stack List 3
        # Stack List 7
        
        current = stack.pop()
        print("current:",current.key)
        
        current = current.right
        # if current:
        #     print("right:",current.key)

class Node:
    def __init__(self, key, left=None, right=None):
        self.key = key
        self.left = left
        self.right = right

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

print_keys_in_order_iterative(root)
