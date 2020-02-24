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


#get edges of the frame in pixels, for plotting
xlim = (0,700)
ylim = (0,500)

sns.distplot(fid['Item2.Value.Item4.mousey'])
sns.distplot(fid['Item2.Value.Item3.mousex'])

wheelxLoc = 100
wheelyLoc = 200

fid['Item2.Value.Item1.wheelx'] = fid['Item2.Value.Item1.wheelx']  + wheelxLoc
fid['Item2.Value.Item2.wheely'] = fid['Item2.Value.Item2.wheely']  + wheelyLoc




sns.jointplot(x='Item2.Value.Item3.mousex', y='Item2.Value.Item4.mousey', data=fid,kind="kde")
sns.jointplot(x='Item2.Value.Item3.mousex', y='Item2.Value.Item4.mousey', data=fid)
sns.jointplot(x='Item2.Value.Item1.wheelx', y='Item2.Value.Item2.wheely', 
              data=fid,xlim=xlim, ylim=ylim,
              marginal_kws=dict(bins=10, rug=False),)






g = (sns.jointplot(x='Item2.Value.Item3.mousex', y='Item2.Value.Item4.mousey', data=fid, color="k")
    .plot_joint(sns.kdeplot, zorder=0, n_levels=6))
#example for later
#g = sns.jointplot(x="x", y="y", data=df, kind="kde", color="m")
#g.plot_joint(plt.scatter, c="w", s=30, linewidth=1, marker="+")
#g.ax_joint.collections[0].set_alpha(0)
#g.set_axis_labels("$X$", "$Y$");