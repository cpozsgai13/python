import matplotlib.pyplot as plt
import networkx as nx

class TreeNode:
    def __init__(self, value=0, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right

def plot_tree(root):
    def add_edges(node, graph, pos={}, x=0, y=0, layer=1):
        if node:
            pos[node.value] = (x, -y)
            graph.add_node(node.value)
            if node.left:
                graph.add_edge(node.value, node.left.value)
                l = x - 1 / layer
                pos.update(add_edges(node.left, graph, pos=pos, x=l, y=y + 1, layer=layer + 1))
            if node.right:
                graph.add_edge(node.value, node.right.value)
                r = x + 1 / layer
                pos.update(add_edges(node.right, graph, pos=pos, x=r, y=y + 1, layer=layer + 1))
        return pos

    graph = nx.DiGraph()
    pos = add_edges(root, graph)
    labels = {node: node for node in graph.nodes()}

    nx.draw(graph, pos, labels=labels, with_labels=True, node_size=2000, node_color='skyblue', font_size=16,
            font_weight='bold')
    plt.show()

def array_to_binary_tree(arr):
    if not arr:
        return None
    
    mid = len(arr) // 2
    node = TreeNode(arr[mid])
    node.left = array_to_binary_tree(arr[:mid])
    node.right = array_to_binary_tree(arr[mid + 1:])
    return node

def main():
    # root = create_test_tree()
    arr = [1, 2, 3, 4, 5, 6, 7, 8, 9]
    root = array_to_binary_tree(arr)
    plot_tree(root)

if __name__ == "__main__":
    main()
