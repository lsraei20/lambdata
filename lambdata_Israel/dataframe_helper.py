"""
Some functions to help cleaning and handling Dataframes!
"""
from sklearn.model_selection import train_test_split


class DfHelper:
    def __init__(self, df):
        self.df = df

    def report_missing_values(self):
        """ Print a pretty report of missing values. """
        print('Columns With Missing Values: \n\n')

        for col in self.df.columns:
            if self.df[col].isna().sum() > 1:
                print(col, 'has')
                print(self.df[col].isna().sum())
                print('Missing Values')
                print('________________')
            elif self.df[col].isna().sum() == 1:
                print(col, 'has')
                print(self.df[col].isna().sum())
                print('Missing Value')
                print('________________')

    def predictive_model_split(self, target):
        """ Create Target and Features data frame as well as train/val/test split """
        x = self.df.drop(target, axis=1)
        y = self.df[target]
        x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.20, random_state=42)
        x_train, x_val, y_train, y_val = train_test_split(x_train, y_train, test_size=0.15, random_state=42)
        return x, x_train, x_val, x_test, y, y_train, y_val, y_test