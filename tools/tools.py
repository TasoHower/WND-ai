import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np

import matplotlib.pyplot as plt
import numpy as np

# 生成示例数据
x = np.linspace(0, 10, 50)
y = np.sin(x)

# 创建图形
plt.figure(figsize=(8, 5))

# 绘制折线图
plt.plot(x, y, label="折线图", color="blue", marker="o")

# 绘制散点图
plt.scatter(x, y, color="red", label="散点图")

# 添加标题和标签
plt.title("title")
plt.xlabel("X 轴")
plt.ylabel("Y 轴")

# 设置 Seaborn 风格
sns.set(style="darkgrid")

# 创建散点图 + 折线图
# sns.lineplot(x=x, y=y, marker="o", label="折线图")
sns.scatterplot(x=x, y=y, color="red", label="散点图")

plt.title("Seaborn 版的折线图 & 散点图")
plt.savefig("test.png")
