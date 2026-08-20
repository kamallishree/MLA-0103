import math
import matplotlib.pyplot as plt
from matplotlib.patches import Ellipse, Rectangle
data = [
    ["True",  "Hot",  "High",   "No"],
    ["True",  "Hot",  "High",   "No"],
    ["False", "Hot",  "High",   "Yes"],
    ["False", "Cool", "Normal", "Yes"],
    ["False", "Cool", "Normal", "Yes"],
    ["True",  "Cool", "High",   "No"],
    ["True",  "Hot",  "High",   "No"],
    ["True",  "Hot",  "Normal", "Yes"],
    ["False", "Cool", "Normal", "Yes"],
    ["False", "Cool", "High",   "Yes"]
]
attributes = ["a1", "a2", "a3"]
def entropy(rows):
    total = len(rows)
    yes = sum(1 for row in rows if row[-1] == "Yes")
    no = sum(1 for row in rows if row[-1] == "No")
    result = 0
    if yes > 0:
        p = yes / total
        result -= p * math.log2(p)
    if no > 0:
        p = no / total
        result -= p * math.log2(p)
    return result
def information_gain(rows, index):
    total_entropy = entropy(rows)
    values = set(row[index] for row in rows)
    weighted_entropy = 0
    for value in values:
        subset = [
            row for row in rows
            if row[index] == value
        ]
        weighted_entropy += (
            len(subset) / len(rows)
        ) * entropy(subset)

    return total_entropy - weighted_entropy
class Node:
    def __init__(self, name, is_leaf=False):
        self.name = name
        self.is_leaf = is_leaf
        self.children = {}
def build_tree(rows, attributes):
    classes = [row[-1] for row in rows]
    if classes.count("Yes") == len(classes):
        return Node("Yes", True)
    if classes.count("No") == len(classes):
        return Node("No", True)
    if len(attributes) == 0:
        yes = classes.count("Yes")
        no = classes.count("No")
        if yes >= no:
            return Node("Yes", True)
        else:
            return Node("No", True)
    gains = []
    for i, attribute in enumerate(attributes):
        gain = information_gain(rows, i)
        gains.append((attribute, i, gain))
    best_attribute, best_index, best_gain = max(
        gains,
        key=lambda x: x[2]
    )
    print(
        "Attribute:", best_attribute,
        "Information Gain:", round(best_gain, 4)
    )
    tree = Node(best_attribute)
    values = set(row[best_index] for row in rows)
    remaining_attributes = [
        attr for attr in attributes
        if attr != best_attribute
    ]
    for value in values:
        subset = [
            row for row in rows
            if row[best_index] == value
        ]
        if len(subset) == 0:
            continue
        new_rows = []
        for row in subset:
            new_row = row[:best_index] + row[best_index + 1:]
            new_rows.append(new_row)
        new_attributes = remaining_attributes.copy()
        child = build_tree(new_rows, new_attributes)
        tree.children[value] = child
    return tree
root = build_tree(data, attributes)
fig, ax = plt.subplots(figsize=(12, 8))
ax.set_xlim(0, 12)
ax.set_ylim(0, 10)
ax.axis("off")
def get_depth(node):
    if node.is_leaf:
        return 1
    return 1 + max(
        get_depth(child)
        for child in node.children.values()
    )
def draw_tree(node, x, y, width, level=0):
    if node.is_leaf:
        shape = Rectangle(
            (x - 0.65, y - 0.35),
            1.3,
            0.7,
            facecolor="white",
            edgecolor="black",
            linewidth=2
        )
        ax.add_patch(shape)
        ax.text(
            x, y, node.name,
            ha="center",
            va="center",
            fontsize=12
        )
        return
    shape = Ellipse(
        (x, y),
        width=2.0,
        height=0.8,
        facecolor="white",
        edgecolor="black",
        linewidth=2
    )
    ax.add_patch(shape)
    ax.text(
        x, y, node.name,
        ha="center",
        va="center",
        fontsize=12
    )
    children = list(node.children.items())
    if len(children) == 1:
        positions = [x]
    else:
        spacing = width / (len(children) - 1)
        positions = [
            x - width / 2 + i * spacing
            for i in range(len(children))
        ]
    child_y = y - 2
    for i, (value, child) in enumerate(children):
        child_x = positions[i]
        ax.plot(
            [x, child_x],
            [y - 0.4, child_y + 0.4],
            "k-"
        )
        ax.text(
            (x + child_x) / 2,
            (y + child_y) / 2 + 0.1,
            value,
            fontsize=11,
            ha="center"
        )
        draw_tree(
            child,
            child_x,
            child_y,
            width / max(len(children), 2),
            level + 1
        )
draw_tree(root, 6, 9, 7)
plt.title("Decision Tree using Entropy", fontsize=16)
plt.show()
