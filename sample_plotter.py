import pandas as pd 
import matplotlib
import matplotlib.pyplot as plt
import numpy as np

# visit https://matplotlib.org/ for more
# examples are https://matplotlib.org/gallery/index.html
# you can replace the data in the examples to get started

data_frame = pd.read_csv("toy.csv")

labels = list(data_frame["name"])
count = list(data_frame["count"])
planned = list(data_frame["planned"])


"""
example 1: adapted from from https://matplotlib.org/gallery/lines_bars_and_markers/barchart.html
"""

x = np.arange(len(labels))  # the label locations
width = 0.35  # the width of the bars

fig, ax = plt.subplots()
rects1 = ax.bar(x - width/2, count, width, label='Current')
rects2 = ax.bar(x + width/2, planned, width, label='Planned')

# Add some text for labels, title and custom x-axis tick labels, etc.
ax.set_ylabel('Count')
ax.set_title('Count of Things')
ax.set_xticks(x)
ax.set_xticklabels(labels)
ax.legend()


def autolabel(rects):
    """Attach a text label above each bar in *rects*, displaying its height."""
    for rect in rects:
        height = rect.get_height()
        ax.annotate('{}'.format(height),
                    xy=(rect.get_x() + rect.get_width() / 2, height),
                    xytext=(0, 3),  # 3 points vertical offset
                    textcoords="offset points",
                    ha='center', va='bottom')


autolabel(rects1)
autolabel(rects2)

fig.tight_layout()

plt.show()


"""
example 2: https://matplotlib.org/gallery/pie_and_polar_charts/pie_and_donut_labels.html
"""

fig, ax = plt.subplots(figsize=(6, 3), subplot_kw=dict(aspect="equal"))

# labels are the same as before

data = count

wedges, texts = ax.pie(data, wedgeprops=dict(width=0.5), startangle=-40)

bbox_props = dict(boxstyle="square,pad=0.3", fc="w", ec="k", lw=0.72)
kw = dict(arrowprops=dict(arrowstyle="-"),
          bbox=bbox_props, zorder=0, va="center")

for i, p in enumerate(wedges):
    ang = (p.theta2 - p.theta1)/2. + p.theta1
    y = np.sin(np.deg2rad(ang))
    x = np.cos(np.deg2rad(ang))
    horizontalalignment = {-1: "right", 1: "left"}[int(np.sign(x))]
    connectionstyle = "angle,angleA=0,angleB={}".format(ang)
    kw["arrowprops"].update({"connectionstyle": connectionstyle})
    ax.annotate(labels[i], xy=(x, y), xytext=(1.35*np.sign(x), 1.4*y),
                horizontalalignment=horizontalalignment, **kw)

# ax.set_title("any title if you want")

plt.show()

