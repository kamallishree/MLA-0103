import math
import matplotlib.pyplot as plt
from matplotlib.patches import Ellipse, Rectangle

data = [
    ["Sunny","Hot","High","Weak","No"],
    ["Sunny","Hot","High","Strong","No"],
    ["Overcast","Hot","High","Weak","Yes"],
    ["Rain","Mild","High","Weak","Yes"],
    ["Rain","Cool","Normal","Weak","Yes"],
    ["Rain","Cool","Normal","Strong","No"],
    ["Overcast","Cool","Normal","Strong","Yes"],
    ["Sunny","Mild","High","Weak","No"],
    ["Sunny","Cool","Normal","Weak","Yes"],
    ["Rain","Mild","Normal","Weak","Yes"],
    ["Sunny","Mild","Normal","Strong","Yes"],
    ["Overcast","Mild","High","Strong","Yes"],
    ["Overcast","Hot","Normal","Weak","Yes"],
    ["Rain","Mild","High","Strong","No"]
]

attributes = ["Outlook","Temperature","Humidity","Wind"]

def entropy(rows):
    total = len(rows)
    yes = sum(row[-1] == "Yes" for row in rows)
    no = total - yes
    result = 0
    if yes:
        p = yes / total
        result -= p * math.log2(p)
    if no:
        p = no / total
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
    classes = [row[-1] for row in rows]
    if classes.count("Yes") == len(classes):
        return Node("Yes", True)
    if classes.count("No") == len(classes):
        return Node("No", True)
    if not attrs:
        return Node("Yes" if classes.count("Yes") >= classes.count("No") else "No", True)

    gains = [(attr, i, information_gain(rows, i)) for i, attr in enumerate(attrs)]
    best_attr, best_index, best_gain = max(gains, key=lambda x: x[2])
    print(best_attr, "=", round(best_gain, 4))

    tree = Node(best_attr)
    remaining = [a for a in attrs if a != best_attr]

    for value in set(row[best_index] for row in rows):
        subset = [row for row in rows if row[best_index] == value]
        new_rows = [row[:best_index] + row[best_index + 1:] for row in subset]
        tree.children[value] = build_tree(new_rows, remaining)

    return tree

root = build_tree(data, attributes)

fig, ax = plt.subplots(figsize=(14, 9))
ax.set_xlim(0, 14)
ax.set_ylim(0, 12)
ax.axis("off")

def draw_tree(node, x, y, width):
    if node.leaf:
        shape = Rectangle((x - 0.7, y - 0.35), 1.4, 0.7, facecolor="white", edgecolor="black", linewidth=2)
        ax.add_patch(shape)
        ax.text(x, y, node.name, ha="center", va="center", fontsize=12)
        return

    shape = Ellipse((x, y), width=2.2, height=0.8, facecolor="white", edgecolor="black", linewidth=2)
    ax.add_patch(shape)
    ax.text(x, y, node.name, ha="center", va="center", fontsize=12)

    children = list(node.children.items())
    count = len(children)
    positions = [x] if count == 1 else [x - width / 2 + i * width / (count - 1) for i in range(count)]
    child_y = y - 2

    for i, (value, child) in enumerate(children):
        child_x = positions[i]
        ax.plot([x, child_x], [y - 0.4, child_y + 0.4], "k-")
        ax.text((x + child_x) / 2, (y + child_y) / 2 + 0.1, value, ha="center", fontsize=11)
        draw_tree(child, child_x, child_y, width / max(count, 2))

draw_tree(root, 7, 11, 10)
plt.title("Decision Tree using Entropy")
plt.show()
