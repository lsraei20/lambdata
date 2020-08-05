### Review


######  1.) The code is very well marked and laid out. The indentation, spacing, and comments makes it very clear where

######  2.) It is very clear what the functions are designed to do. The logic behind it is very clear.

######  3.) The only criticism I have is that the code inside the for loop seems a little repetitive. Would it be possible to write it as:
            f'${col:,.0f} has {self.df[col].isna().sum():,.0f} missing values'
