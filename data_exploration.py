# -*- coding: utf-8 -*-
"""
Created on Fri Jun  4 17:07:59 2021

@author: 100431522
"""
def explore_data(dataset, start, end, rows_and_columns=False):
    """ slice and print out a dataset between start and end, and
        if necessary, print out the number of rows and columns
    """
    dataset_slice = dataset[start:end]    
    for row in dataset_slice:
        print(row)
        print('\n') # adds a new (empty) line after each row

    if rows_and_columns:
        print('Number of rows:', len(dataset))
        print('Number of columns:', len(dataset[0]))