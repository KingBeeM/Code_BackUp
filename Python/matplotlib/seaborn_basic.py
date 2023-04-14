import matplotlib.pyplot as plt
import seaborn as sns

# tips data
tips = sns.load_dataset("tips")
tips.head()

# seaborn displot(barchart)
sns.displot(x = "tip", data = tips)

# seaborn displot detail
fig, axs = plt.subplots()

# Error, because it's not supported in displot()
# sns.displot(x = "tip", data = tips, ax=axs)
# sns.histoplot() supports it.

sns.histplot(x = "tip", data = tips, ax=axs)
plt.show()

# [1 x 2] Partition
fig, axs = plt.subplots(nrows=1, ncols=2)

axs[0].plot([1, 2, 3])
axs[0].set_title("matplotlib plot")

sns.histplot(x = "tip", data = tips, ax=axs[1])
axs[1].set_title("seaborn histplot")

plt.tight_layout()
plt.show()

# seaborn countplot(barchart)
fig, axs = plt.subplots()
sns.countplot(x="day", data=tips)
plt.show()

# seaborn countplot detail : order
fig, axs = plt.subplots()
sns.countplot(x="day", 
              data=tips, 
              order=tips["day"].value_counts().index)
print(tips["day"].value_counts().index)
plt.show()

# seaborn countplot detail : text
fig, axs = plt.subplots()
axs = sns.countplot(x="day", data=tips, order=tips["day"].value_counts().index)
print("grape type :", type(axs))
for p in axs.patches:
  print(p, type(p))
  height = p.get_height()
  axs.text(x = p.get_x() + p.get_width() / 2,
           y = height + 3,
           s = height,
           ha = "center",
           size = 9)
axs.set_ylim(-1, 100)
plt.show()
