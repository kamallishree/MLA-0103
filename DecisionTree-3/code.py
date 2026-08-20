import math
import matplotlib.pyplot as plt
from matplotlib.patches import Ellipse, Rectangle

data = [
    ["+","T","T"],
    ["+","T","T"],
    ["-","T","F"],
    ["+","F","F"],
    ["-","F","T"],
    ["-","F","T"]
]

attributes = ["a1","a2"]

def entropy(rows):
    total = len(rows)
    pos = sum(row[0] == "+" for row in rows)
    neg = total - pos
    result = 0
    if pos:
        p = pos / total
        result -= p * math.log2(p)
    if neg:
        p = neg / total
        result -= p * math.log2(p)
    return result

def information_gain(rows, index):
    total_entropy = entropy(rows)
    weighted_entropy = 0
    for value in set(row[index] for row in rows):
        subset = [row for row in rows if row[index] == value]
        weighted_entropy += len(subset) / len(rows) * entropy(subset)
    return total_entropy - weighted_entropy

class Node:
    def __init__(self, name, leaf=False):
        self.name = name
        self.leaf = leaf
        self.children = {}

def build_tree(rows, attrs):
    classes = [row[0] for row in rows]

    if classes.count("+") == len(classes):
        return Node("+", True)
    if classes.count("-") == len(classes):
        return Node("-", True)

    if not attrs:
        return Node("+" if classes.count("+") >= classes.count("-") else "-", True)

    gains = [(attr, i + 1, information_gain(rows, i + 1)) for i, attr in enumerate(attrs)]
    best_attr, best_index, best_gain = max(gains, key=lambda x: x[2])

    print(best_attr, "=", round(best_gain, 4))

    tree = Node(best_attr)
    remaining = [a for a in attrs if a != best_attr]

    for value in set(row[best_index] for row in rows):
        subset = [row for row in rows if row[best_index] == value]

        new_rows = []
        for row in subset:
            new_rows.append([row[0]] + [row[i] for i in range(1, len(row)) if i != best_index])

        tree.children[value] = build_tree(new_rows, remaining)

    return tree

root = build_tree(data, attributes)

fig, ax = plt.subplots(figsize=(10, 7))
ax.set_xlim(0, 10)
ax.set_ylim(0, 9)
ax.axis("off")

def draw_tree(node, x, y, width):
    if node.leaf:
        shape = Rectangle((x - 0.6, y - 0.3), 1.2, 0.6, facecolor="white", edgecolor="black", linewidth=2)
        ax.add_patch(shape)
        ax.text(x, y, node.name, ha="center", va="center", fontsize=12)
        return

    shape = Ellipse((x, y), width=2, height=0.8, facecolor="white", edgecolor="black", linewidth=2)
    ax.add_patch(shape)
    ax.text(x, y, node.name, ha="center", va="center", fontsize=12)

    children = list(node.children.items())
    count = len(children)
    positions = [x] if count == 1 else [x - width / 2 + i * width / (count - 1) for i in range(count)]
    child_y = y - 2

    for i, (value, child) in enumerate(children):
        child_x = positions[i]
        ax.plot([x, child_x], [y - 0.4, child_y + 0.3], "k-")
        ax.text((x + child_x) / 2, (y + child_y) / 2, value, ha="center", fontsize=11)
        draw_tree(child, child_x, child_y, width / max(count, 2))

draw_tree(root, 5, 8, 6)
plt.title("Decision Tree using Entropy")
plt.show()
