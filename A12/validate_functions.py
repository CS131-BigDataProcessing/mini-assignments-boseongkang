import pandas as pd

def validate_sex(df):
    if df.isnull().any():
        return False
    for sex in df:
        if sex != 'M' & sex != 'F':
            return False
    return True

def validate_age(df):
    if df.isnull().any():
        return False
    for age in df:
        if age < 1 or age > 100:
            return False
    return True
