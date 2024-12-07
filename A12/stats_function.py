import pandas as pd
import numpy as np

def calculate_mean_med(df):
    if df.isnull().any():
        return False, False

    mean_age = np.mean(df)
    med_age = np.median(df)
    
    return mean_age,med_age
