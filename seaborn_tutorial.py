import seaborn as sns
import matplotlib.pyplot as plt
sns.set_theme()
tips = sns.load_dataset("tips")
#sns.relplot(data=tips,x="total_bill",y="tip",col="sex",hue="smoker",style="smoker",size="size",)

fmri=sns.load_dataset("fmri")
#sns.relplot(data=fmri,kind="line",x="timepoint",y="signal",col="region",hue="event",style="event")
#plt.show()

#  Distributional plots
sns.displot(data=tips,x="total_bill",col="time",kde=True)


plt.show()
