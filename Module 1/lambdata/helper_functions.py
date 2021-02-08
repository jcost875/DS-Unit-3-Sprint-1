"""This file will define common use functions"""

# This function will count and return total nulls for a dataframe
def null_count(df):
    X = df.isnull().sum().sum()
    return X

# This function will perform a train/test split
def train_test_split(df, frac):
    from sklearn.model_selection import train_test_split
    train, test = train_test_split(df, train_size=frac, test_size=(1-frac), random_state=42)
    return train, test

# This function will perform a split of a date column into 3 unique
# columns for day, month & year
def split_dates(df):
    for col in df.columns:
        if df[col].dtype == 'object':
            try:
                df[col] = pd.to_datetime(df[col])
                df['month']=pd.DatetimeIndex(df[col]).month
                df['day']=pd.DatetimeIndex(df[col]).day
                df['year']=pd.DatetimeIndex(df[col]).year
            except ValueError:
                pass
    return df
