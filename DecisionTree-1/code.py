import matplotlib.pyplot as plt
from matplotlib.patches import Ellipse, Rectangle
fig, ax = plt.subplots(figsize=(12, 8))
ax.set_xlim(0, 12)
ax.set_ylim(0, 10)
ax.axis("off")
def oval(x, y, text):
    shape = Ellipse(
        (x, y),
        width=2.2,
        height=0.8,
        facecolor="white",
        edgecolor="black",
        linewidth=2
    )
    ax.add_patch(shape)
    ax.text(x, y, text, ha="center", va="center", fontsize=12)
def box(x, y, text):
    shape = Rectangle(
        (x - 0.7, y - 0.35),
        1.4,
        0.7,
        facecolor="white",
        edgecolor="black",
        linewidth=2
    )
    ax.add_patch(shape)
    ax.text(x, y, text, ha="center", va="center", fontsize=12)
def line(x1, y1, x2, y2):
    ax.plot([x1, x2], [y1, y2], "k-")
oval(6, 9, "Outlook")
oval(3, 6.8, "Humidity")
box(6, 6.8, "Yes")
oval(9, 6.8, "Wind")
line(5.1, 8.7, 3, 7.2)
line(6, 8.6, 6, 7.2)
line(6.9, 8.7, 9, 7.2)
ax.text(4.2, 8.0, "Sunny", fontsize=11)
ax.text(6.1, 8.0, "Overcast", fontsize=11)
ax.text(7.8, 8.0, "Rain", fontsize=11)
box(2, 4.7, "No")
box(4, 4.7, "Yes")
line(2.5, 6.5, 2, 5.05)
line(3.5, 6.5, 4, 5.05)
ax.text(2.0, 5.7, "High", fontsize=11)
ax.text(3.7, 5.7, "Normal", fontsize=11)
box(8, 4.7, "Yes")
box(10, 4.7, "No")
line(8.5, 6.5, 8, 5.05)
line(9.5, 6.5, 10, 5.05)
ax.text(7.9, 5.7, "Weak", fontsize=11)
ax.text(9.7, 5.7, "Strong", fontsize=11)
plt.title("Decision Tree - Play Tennis", fontsize=16)
plt.show()
