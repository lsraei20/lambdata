# lambdata
Cool package with DS functions!

TestPYPI package link:
https://test.pypi.org/project/lambdata-Israel/


### dataframe_helper 
- report_missing_values: 

Check a dataframe for nulls, print/report them in a nice "pretty" format.

- predictive_model_split:

It takes 2 parameters 'df': Data Frame to use & 'target': column name to use as a target.
It will create both the features and target dataframes and make a train/validation/test split 
It returns values in the following order:
X, X_train, X_val, X_test, y, y_train, y_val, y_test
