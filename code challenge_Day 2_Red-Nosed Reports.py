# -*- coding: utf-8 -*-
"""
Created by Andrea Unrau, June 17, 2026
for samdesk opening: Junior Machine Learning Engineer - Alerts Team
"""

import pandas as pd

           
#%% Define some helper functions
 
def check_first_two_indices_are_different(row):
        return row.iloc[0] != row.iloc[1]

    

def check_is_increasing(row):
    """
    Returns True if the value at index 0 is less than the value at index 1.
    Returns False otherwise.
    
    Parameters:
        row (pandas.Series): A series containing at least two elements.
    
    Returns:
        bool: True if row.iloc[0] < row.iloc[1], otherwise False.
    """
    
    is_increasing = True
    
    if (row.iloc[0] < row.iloc[1]):
        return is_increasing
    else:
        is_increasing = False
        return is_increasing
    
    
    
def check_is_safe(row, min_diff, max_diff, is_increasing):
    """
    Checks whether a sequence is "safe" based on the differences between
    consecutive values.
 
    For an increasing sequence, each difference between adjacent values
    from left to right must be between min_diff and max_diff (inclusive).
 
    For a decreasing sequence, the same check is performed in reverse order,
    treating the sequence as increasing from right to left.
 
    Parameters:
        row (pandas.Series): Sequence of numeric values.
        min_diff (int or float): Minimum allowed difference between consecutive values.
        max_diff (int or float): Maximum allowed difference between consecutive values.
        is_increasing (bool): True if the sequence is expected to be
            increasing, False if it is expected to be decreasing.
 
    Returns:
        bool: True if all consecutive differences are within the allowed
            range, otherwise False.
    """

    if is_increasing:
        is_safe = True
        i = 1
        while is_safe and i in range(len(row)):
            is_safe = min_diff <= (row.iloc[i] - row.iloc[i-1]) <= max_diff
            i += 1
    else:
        # since the sequence is decreasing, we can check from the end if it is increasing
        is_safe = True
        i = len(row) - 1
        while is_safe and i > 0:
            is_safe = min_diff <= (row.iloc[i-1] - row.iloc[i]) <= max_diff
            i -= 1
    
    return is_safe
    


#%%    
    
def main():
    
    safe = 0
    min_diff = 1
    max_diff = 3
    
    
    df = pd.DataFrame(
        [
            [7, 6, 4, 2, 1],
            [1, 2, 7, 8, 9],
            [9, 7, 6, 2, 1],
            [1, 3, 2, 4, 5],
            [8, 6, 4, 4, 1],
            [1, 3, 6, 7, 9]
        ],
        columns=['A', 'B', 'C', 'D', 'E']
    )
    

    for _, row in df.iterrows():
        if len(row) > 1 and check_first_two_indices_are_different(row):
            is_increasing = check_is_increasing(row)
            is_safe = check_is_safe(row, min_diff, max_diff, is_increasing)
            safe += is_safe
            
    print(f"{safe} report(s) are safe.")
    
    
    
if __name__ == "__main__":
    main()
    
    