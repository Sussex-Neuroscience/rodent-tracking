import os
import pandas as pd
import seaborn as sns
import numpy as np



filepath = "/mnt/d/repositories/rodent-tracking/test_data/all_data1.csv"

fid = pd.read_csv(filepath)

# print all the variables names
print(fid.keys())

# set some variables
wheelMoving = fid["Item1.Item6.wheelmoving"]
mouseMoving = fid["Item1.Item3.mousemoving"]
timeInterval = fid['Item1.Item7.frameinterval']

#get running wheel time
whellTime = timeInterval[wheelMoving].sum()

#get animal moving time
mouseTime = timeInterval[mouseMoving].sum()

sns.distplot(fid['Item2.Value.Item4.mousey'])
sns.distplot(fid['Item2.Value.Item3.mousex'])

df = pd.DataFrame([fid['Item2.Value.Item3.mousex'],fid['Item2.Value.Item4.mousey']])

sns.jointplot(x='Item2.Value.Item3.mousex', y='Item2.Value.Item4.mousey', data=fid,kind="kde")

#example for later
#g = sns.jointplot(x="x", y="y", data=df, kind="kde", color="m")
#g.plot_joint(plt.scatter, c="w", s=30, linewidth=1, marker="+")
#g.ax_joint.collections[0].set_alpha(0)
#g.set_axis_labels("$X$", "$Y$");