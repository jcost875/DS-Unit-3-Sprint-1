"""This file will define common use functions"""

# This will define a class for the dataframe to pass through the helper functions
class HelperClass:
    """This class will create dataframes to be passed through helper functions"""

    def __init__(self, DataFrame):
        self.DataFrame = DataFrame

# This function will count and return total nulls for a dataframe
    def null_count(self):
        num_null = self.DataFrame.isnull().sum().sum()
        return num_null

# This will randomize the dataframe
    def randomize(self, seed):
        df = self.DataFrame.sample(frac=1, random_state=seed)
        return df

# This will add a list as a column in a given dataframe
    def list_2_series(self, list):
        self.DataFrame[list] = list
        return self.DataFrame

# This function will perform a train/test split
    def train_test_split(self, frac):
        train = self.DataFrame.sample(frac=frac, random_state=42)
        test = self.DataFrame.drop(train.index)
        return train, test

# TODO: This function will perform a split of a date column into 3 
# unique columns for day, month & year
# def split_dates(series):
#   import pandas as pd
#    df = pd.DataFrame(series)
#    df = pd.to_datetime(df)
#    df['month']=pd.DatetimeIndex(df).month
#    df['day']=pd.DatetimeIndex(df).day
#    df['year']=pd.DatetimeIndex(df).year
#    return df
