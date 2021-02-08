"""This file will define common use functions"""

# This function will count and return total nulls for a dataframe
def null_count(df):
    X = df.isnull().sum().sum()
    return X

# This will randomize the dataframe
def randomize(df, seed):
    df = df.sample(frac=1, random_state=seed)
    return df

# This function will perform a train/test split
def train_test_split(df, frac):
    import pandas as pd
    train = df.sample(frac=frac, random_state=42)
    test = df.drop(train.index)
    return train, test

# TODO: This function will perform a split of a date column into 3 
# unique columns for day, month & year
# def split_dates(df):
#    import pandas as pd
#    df = pd.to_datetime(df)
#    df['month']=pd.DatetimeIndex(df).month
#    df['day']=pd.DatetimeIndex(df).day
#    df['year']=pd.DatetimeIndex(df).year
#    return df
