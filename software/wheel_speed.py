import pandas as pd
#import seaborn as sns
import matplotlib.pyplot as plt
import os
import numpy as np
#filePath = "C:\Users\andre\Documents\GitHub\rodent-tracking\test_data\"

filePath = os.getcwd()


oneDirUp = os.path.dirname(filePath)
filePath = oneDirUp + "/test_data/"
fileName = "tracking_wheel2020-02-10T10_22_19.csv"

#open a csv file and store contents as a dataframe in fid
fid = pd.read_csv(filePath+fileName)


#drop the first 20 entries. (temp since there was a camera adjustment in the start of this recording.)
fid = fid.drop(list(range(0,21)))

#find not NaN values
detectIndex = fid['Value.X'].notna()

#get time stamps of non nan values
times = fid['Timestamp'][detectIndex][:]

#transform the series into a datetime series, so that we can make mathematical operations on them
times = pd.to_datetime(times)

# subtract each timepoint N from N+1 (to get the time interval between each pass of the wheel through the video marker)
times.diff()

# subtract each index N from N+1. 
# values =< 2 indicate the times the wheel marker was going through the threshold window, so we want to ignore those.
wheelInd = np.diff(times.index)>1
#add an False entry to the end so that this array can be used to index "times"
wheelInd = np.append(wheelInd,False)

#these are all the time stamps (the first of each detection burst) where the wheel marker was detected
times[wheelInd]
interval = list(times[wheelInd].diff())

plt.hist(interval[1:])

np.array()


#get the unique values
#times.loc[wheelInd] = np.unique(wheelInd)

#find non nan values

#check how much time in between non nan values

#decide on a minimal interval for running bouts

#detect running bouts

#in each running bout get angular velocity

# transform it to linear velocity

# get acceleration

# out put number of running bouts,

# velocity and acceleration traces for each bout

# all in a csv file? so that it can later be combined with
# the other files for each animal.

