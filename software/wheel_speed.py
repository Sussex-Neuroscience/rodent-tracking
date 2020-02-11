import pandas as pd
import os
#filePath = "C:\Users\andre\Documents\GitHub\rodent-tracking\test_data\"

filePath = os.getcwd()


oneDirUp = os.path.dirname(filePath)
filePath = oneDirUp + "/test_data/"
fileName = "tracking_wheel2020-02-10T10_22_19.csv"

fid = pd.read_csv(filePath+fileName)

fid = fid[20:]

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

