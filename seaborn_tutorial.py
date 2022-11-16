import seaborn as sns
import matplotlib.pyplot as plt
sns.set_theme()
tips = sns.load_dataset("tips")
#sns.relplot(data=tips,x="total_bill",y="tip",col="sex",hue="smoker",style="smoker",size="size",)

fmri=sns.load_dataset("fmri")
#sns.relplot(data=fmri,kind="line",x="timepoint",y="signal",col="region",hue="event",style="event")
#plt.show()


import random
x=[i for i in range(100)]
y=[i**2 + random.random() for i in x]

sns.relplot(x=x,y=y,kind="line")
plt.show()
