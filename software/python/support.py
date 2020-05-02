import pandas as pd


def rename_rows(pandaDF):
    """
    this function renames the columns in the data frame so that is easier
    to call them. This is due to the fact that I wasn't able to properly rename the variables
    coming out of Bonsai.
    
    There is probably a better way of doing this using Bonsai
    """
    
    for key in pandaDF.keys():
        secondDot = key.find(".",6)
        pandaDF = pandaDF.rename(columns = {key:key[secondDot+1:]})
    
    return pandaDF

def load_n_join_DFs(csvFiles):
    """
    take a list with csv file names and load all of them in one panda dataframe 
    """
    allData = pd.DataFrame()
    for item in csvFiles:
        fid = pd.read_csv(item)
        fid = rename_rows(fid)
        allData = allData.append(fid)
    
    return allData