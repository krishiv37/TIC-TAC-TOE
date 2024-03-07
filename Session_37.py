import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd

x = [3,5,6,8]
y = [5,7,9,11]

df = pd.DataFrame({"x" : x,"y" : y})

sns.lineplot(x="x",y="y",data=df)
plt.show()
df3 = sns.load_dataset("tips")
df3
sns.lineplot(x="total_bill",y="tip",data=df3,hue="smoker",palette = "Set2",style="smoker",markers=["o",">"])
plt.show()