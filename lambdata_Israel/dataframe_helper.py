"""
Some functions to help cleaning and handling Dataframes!
"""
from sklearn.model_selection import train_test_split

def report_missing_values(df):
    """ Print a pretty report of missing values. """
    print('Columns With Missing Values: \n\n')

    for col in df.columns:
        if df[col].isna().sum() > 1:
            print(col, 'has')
            print(df[col].isna().sum())
            print('Missing Values')
            print('________________')
        elif df[col].isna().sum() == 1:
            print(col, 'has')
            print(df[col].isna().sum())
            print('Missing Value')
            print('________________')


def predictive_model_split(df, target):
    """ Create Target and Features data frame as well as train/val/test split """
    X = df.drop(target, axis=1)
    y = df[target]
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.20, random_state=42)
    X_train, X_val, y_train, y_val = train_test_split(X_train, y_train, test_size=0.15, random_state=42)
    return X, X_train, X_val, X_test, y, y_train, y_val, y_test
