from env import host, user, password
import pandas as pd
import numpy as np

from sklearn.model_selection import train_test_split
import sklearn.preprocessing

def acquire_mall():
    '''
    Grab data from Codeup SQL server
    '''
    sql_query = ''' select *
    from customers
    '''
    # make the connection to codeup sequel server
    connection = f'mysql+pymysql://{user}:{password}@{host}/mall_customers'
    # Assign the df
    df = pd.read_sql(sql_query, connection)
    return df

def mall_dummies(df):
    '''This funciton takes in a df
    takes the gender column and encodes it
    merges the dummy with the df
    drops the original gender column
    returns df'''
    # split the gender column
    dummy_df = pd.get_dummies(df[["gender"]], drop_first=False)
    # merge dummy and df
    df = pd.concat([df, dummy_df], axis=1)
    # drop gender
    df = df.drop(["gender"], axis=1)
    return df

def split_mall(df):
    '''This fuction takes in a df 
    splits into train, test, validate
    return: three pandas dataframes: train, validate, test
    '''
    # split the focused zillow data
    train_validate, test = train_test_split(df, test_size=.2, random_state=1234)
    train, validate = train_test_split(train_validate, test_size=.3, 
                                       random_state=1234)
    return train, validate, test

def scale_mall(train, validate, test):
    '''this function takes in train, validate, and test
    create a scaler
    fit scaler
    create train_scaled, validate_scaled, and test_scaled
    and turn each of them into data frames
    returns train_scaled, validate_scaled, test_scaled
    '''
    # Make the thing
    scaler = sklearn.preprocessing.MinMaxScaler()
    # fit the thing
    scaler.fit(train)
    # tun them
    train_scaled = scaler.transform(train)
    validate_scaled = scaler.transform(validate)
    test_scaled = scaler.transform(test)
    # hey pandas make them into dataframes
    train_scaled = pd.DataFrame(train_scaled, columns=train.columns)
    validate_scaled = pd.DataFrame(validate_scaled, columns=train.columns)
    test_scaled = pd.DataFrame(test_scaled, columns=train.columns)
    # return them
    return train_scaled, validate_scaled, test_scaled