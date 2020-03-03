import os

import pandas as pd
import seaborn as sns
import numpy as np
import matplotlib.pyplot as plt


#filepath = "/mnt/d/repositories/rodent-tracking/test_data/all_data_olenna2020-02-24T18_07_54.csv"
filepath = "~/repositories/sussex_neuro/rodent-tracking/test_data/all_data_olenna2020-02-24T18_07_54.csv"
fid = pd.read_csv(filepath)

# print all the variables names
print(fid.keys())

#rename indexes so it is easier to call them 
# there is probably a better way of setting their names in Bonsai...




for key in fid.keys():
    print(key)
    secondDot = key.find(".",6)
    fid = fid.rename(columns = {key:key[secondDot+1:]})



# set some variables
wheelROIY = fid["wheel.Item1.wheelROI.Y"]
wheelROIX = fid["wheel.Item1.wheelROI.Y"]
wheelX = fid["wheel.Item2.wheel.Centroid.X"]
wheelY = fid["wheel.Item2.wheel.Centroid.Y"]


wheelMoving = fid["wheelmoving"]
mouseMoving = fid["mousemoving"]
timeInterval = fid["frameinterval"]


mouseX = fid["mouse.mouse.Centroid.X"]
mouseY = fid["mouse.mouse.Centroid.Y"]






#travelled distance
'''
if there was only the mouse on the cage, the travelled distance would be: 
- given by pytagoras a2 = b2 X c2 for where b and c are x and y
dimensions, and their magnitude is the difference between 2 consecutive frames.

But the mouse has a wheel in its cage, so we need to add the "distance" the wheel
travelled to the distance travelled by the animal (since while running on the wheel,
the animal is static in relation to the cage).

so in the end we want the distance travelled by the mouse while it was NOT on 
the wheel, plus the distance travelled by the wheel, while the wheel was moving

'''
##mouse
###distance X
mouseDistX = np.diff(mouseX.dropna())

###distance y
mouseDistY = np.diff(mouseY.dropna())

mouseTotalDist = np.sqrt(mouseDistX**2+mouseDistY**2) 

np.sum(mouseTotalDist)

#get running wheel time
wheelTime = timeInterval[wheelMoving].sum()

#get animal moving time
mouseTime = timeInterval[mouseMoving].sum()

#get edges of the frame in pixels, for plotting
#cameraXEdge = fid["mouse.mouseROI.width"]
#cameraYEdge = fid["mouse.mouseROI.width"]

cameraXEdge = 680
cameraYEdge = 500

xlim = (0,cameraXEdge)
ylim = (0,cameraYEdge)

sns.distplot(fid['mouse.mouse.Centroid.X'])
sns.distplot(fid['mouse.mouse.Centroid.Y'])

#origin location in pixels of the wheel tracking marker on the video feed
wheelxLoc = fid["wheel.Item1.wheelROI.X"][0]
wheelyLoc = fid["wheel.Item1.wheelROI.Y"][0]

fid['wheel.Item2.wheel.Centroid.X'] = fid['wheel.Item2.wheel.Centroid.X']  + wheelxLoc
fid['wheel.Item2.wheel.Centroid.Y'] = fid['wheel.Item2.wheel.Centroid.Y']  + wheelyLoc




sns.jointplot(x='Item2.Value.Item3.mousex', y='Item2.Value.Item4.mousey', data=fid,kind="kde")
sns.jointplot(x='Item2.Value.Item3.mousex', y='Item2.Value.Item4.mousey', data=fid)

sns.jointplot(x='wheel.Item2.wheel.Centroid.X', y='wheel.Item2.wheel.Centroid.Y', 
              data=fid,xlim=xlim, ylim=ylim,kind="kde",
              #marginal_kws=dict(bins=10, rug=False),
              )
sns.jointplot(x='mouse.mouse.Centroid.X', y='mouse.mouse.Centroid.Y', 
              data=fid,xlim=xlim, ylim=ylim,kind="hex",
              #marginal_kws=dict(bins=10, rug=False),
              )


#plt.hist(x = [fid['mouse.mouse.Centroid.X'].dropna()],bins = int(680/20))
plt.hist(x = [fid['mouse.mouse.Centroid.X'].dropna()],bins = 40)
plt.hist(x = [fid['mouseyvel'].dropna()],range=[-3000,3000],bins=200)
#example for later
#g = sns.jointplot(x="x", y="y", data=df, kind="kde", color="m")
#g.plot_joint(plt.scatter, c="w", s=30, linewidth=1, marker="+")
#g.ax_joint.collections[0].set_alpha(0)
#g.set_axis_labels("$X$", "$Y$");