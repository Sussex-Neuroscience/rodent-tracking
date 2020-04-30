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
        fid = pandaDF.rename(columns = {key:key[secondDot+1:]})
    
    return fid

def load_n_join_DFs(fileList):
    pass