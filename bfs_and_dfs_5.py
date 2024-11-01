import uuid
import networkx as nx
import matplotlib.pyplot as plt
from matplotlib.colors import to_hex, to_rgb
import colorsys

class Node:
    def __init__(self, key, color="skyblue"):
        self.left = None
        self.right = None
        self.val = key
        self.color = color  # Додатковий аргумент для зберігання кольору вузла
        self.id = str(uuid.uuid4())  # Унікальний ідентифікатор для кожного вузла

def add_edges(graph, node, pos, x=0, y=0, layer=1):
    if node is not None:
        graph.add_node(node.id, color=node.color, label=node.val)  # Використання id та збереження значення вузла
        if node.left:
            graph.add_edge(node.id, node.left.id)
            l = x - 1 / 2 ** layer
            pos[node.left.id] = (l, y - 1)
            l = add_edges(graph, node.left, pos, x=l, y=y - 1, layer=layer + 1)
        if node.right:
            graph.add_edge(node.id, node.right.id)
            r = x + 1 / 2 ** layer
            pos[node.right.id] = (r, y - 1)
            r = add_edges(graph, node.right, pos, x=r, y=y - 1, layer=layer + 1)
    return graph

def draw_tree(tree_root, visited_nodes=None):
    tree = nx.DiGraph()
    pos = {tree_root.id: (0, 0)}
    tree = add_edges(tree, tree_root, pos)

    # Використання кольорів для відвіданих вузлів
    colors = [visited_nodes[node[0]] if visited_nodes and node[0] in visited_nodes else node[1]['color']
              for node in tree.nodes(data=True)]
    labels = {node[0]: node[1]['label'] for node in tree.nodes(data=True)}  # Використовуйте значення вузла для міток

    plt.figure(figsize=(8, 5))
    nx.draw(tree, pos=pos, labels=labels, arrows=False, node_size=2500, node_color=colors)
    plt.show()

def get_color_gradient(steps, base_color="#1296F0"):
    """
    Генерує кольори від темного до світлого для заданої кількості кроків.
    """
    base_rgb = to_rgb(base_color)
    h, s, v = colorsys.rgb_to_hsv(*base_rgb)
    return [to_hex(colorsys.hsv_to_rgb(h, s, v * (0.5 + i / (2 * steps)))) for i in range(steps)]

def bfs_visualize(root):
    if not root:
        return
    
    queue = [root]
    visited_colors = {}
    gradient = get_color_gradient(len(queue))

    idx = 0
    while queue:
        node = queue.pop(0)
        visited_colors[node.id] = gradient[idx]
        idx += 1

        draw_tree(root, visited_nodes=visited_colors)
        
        if node.left:
            queue.append(node.left)
        if node.right:
            queue.append(node.right)

def dfs_visualize(root):
    if not root:
        return
    
    stack = [root]
    visited_colors = {}
    gradient = get_color_gradient(len(stack))

    idx = 0
    while stack:
        node = stack.pop()
        visited_colors[node.id] = gradient[idx]
        idx += 1

        draw_tree(root, visited_nodes=visited_colors)
        
        # Для обходу DFS додаємо правий вузол перед лівим, щоб лівий оброблявся першим
        if node.right:
            stack.append(node.right)
        if node.left:
            stack.append(node.left)

# Створення дерева
root = Node(0)
root.left = Node(4)
root.left.left = Node(5)
root.left.right = Node(10)
root.right = Node(1)
root.right.left = Node(3)

# Візуалізація обходу в ширину
print("Обхід у ширину (BFS):")
bfs_visualize(root)

# Візуалізація обходу в глибину
print("Обхід у глибину (DFS):")
dfs_visualize(root)
