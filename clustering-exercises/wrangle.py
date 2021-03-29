from env import host, user, password
import pandas as pd
import numpy as np


def acquire_zillow():
    '''
    Grab data from Codeup SQL server
    '''
    sql_query = '''select *
    from properties_2017
    left join airconditioningtype using(airconditioningtypeid)
    left join architecturalstyletype using(architecturalstyletypeid)
    left join buildingclasstype using(buildingclasstypeid)
    left join heatingorsystemtype using(heatingorsystemtypeid)
    left join storytype using(storytypeid)
    left join typeconstructiontype using(typeconstructiontypeid)
    join (select parcelid, max(transactiondate) as transactiondate
                from predictions_2017
                group by parcelid) as pred_17
        using(parcelid)
    where transactiondate like '2017-%%-%%'
        and parcelid in(
            select distinct parcelid)
            and latitude is not null
                and longitude is not null;'''
    # make the connection to codeup sequel server
    connection = f'mysql+pymysql://{user}:{password}@{host}/zillow'
    # Assign the df
    df = pd.read_sql(sql_query, connection)
    return df

def clean_zillow(df):
    '''This function takes in the df
    applies all the cleaning funcitons previously created'''
    df = wrangle.only_one_unit_homes(df)
    df = wrangle.drop_50_pct_null(df)
    return df

def missing_zero_values_table(df):
        zero_val = (df == 0.00).astype(int).sum(axis=0)
        null_count = df.isnull().sum()
        mis_val_percent = 100 * df.isnull().sum() / len(df)
        mz_table = pd.concat([zero_val, null_count, mis_val_percent], axis=1)
        mz_table = mz_table.rename(
        columns = {0 : 'Zero Values', 1 : 'null_count', 2 : '% of Total Values'})
        mz_table['Total Zeroes + Null Values'] = mz_table['Zero Values'] + mz_table['null_count']
        mz_table['% Total Zero + Null Values'] = 100 * mz_table['Total Zeroes + Null Values'] / len(df)
        mz_table['Data Type'] = df.dtypes
        mz_table = mz_table[
            mz_table.iloc[:,1] >= 0].sort_values(
        '% of Total Values', ascending=False).round(1)
        print ("Your selected dataframe has " + str(df.shape[1]) + " columns and " + str(df.shape[0]) + " Rows.\n"      
            "There are " +  str((mz_table['null_count'] != 0).sum()) +
          " columns that have NULL values.")
#         mz_table.to_excel('D:/sampledata/missing_and_zero_values.xlsx', freeze_panes=(1,0), index = False)
        return mz_table

def null_tables(df):
    '''This function will take in a df
    counts the number of missing features
    counts the number of missing rows
    finds the percent of missing columns
    returns a table with each of theses are features'''
    # Gotta set up the new Dataframes info
    table_nulls = df.isnull().sum(axis =1).value_counts().sort_index(ascending=False)
    # Make it into an officail df
    table_nulls = pd.DataFrame(table_nulls)
    # reset the index
    table_nulls.reset_index(level=0, inplace=True)
    # create the columns num_cols_missing and num_rows_missing
    table_nulls.columns= ['num_cols_missing', 'num_rows_missing']
    # now I need to add the percent column
    table_nulls['pct_cols_missing']= round((table_nulls.num_cols_missing /df.shape[1]) * 100, 2)
    return table_nulls

def only_one_unit_homes(df):
    '''This function takes in the zillow df
    removes rows where the propertylandusetype id is not a single unite
    returns a new df'''
    # Remove rows where propertylandusetypeid is less than 260
    clean_it = df.loc[df['propertylandusetypeid'] < 260].index
    df.drop(clean_it , inplace=True)
    # Remove rows where propertylandusetypeid is 267
    clean_it = df.loc[df['propertylandusetypeid'] == 267].index
    df.drop(clean_it , inplace=True)
        # Remove rows where propertylandusetypeid is 267
    clean_it = df.loc[df['propertylandusetypeid'] == 268].index
    df.drop(clean_it , inplace=True)
        # Remove rows where propertylandusetypeid is 267
    clean_it = df.loc[df['propertylandusetypeid'] == 269].index
    df.drop(clean_it , inplace=True)
        # Remove rows where propertylandusetypeid is 267
    clean_it = df.loc[df['propertylandusetypeid'] == 270].index
    df.drop(clean_it , inplace=True)
        # Remove rows where propertylandusetypeid is 267
    clean_it = df.loc[df['propertylandusetypeid'] == 271].index
    df.drop(clean_it , inplace=True)
    # Remove rows where propertylandusetypeid is 269
    clean_it = df.loc[df['propertylandusetypeid'] == 274].index
    df.drop(clean_it , inplace=True)
    # Remove rows where propertylandusetypeid is less than 260
    clean_it = df.loc[df['propertylandusetypeid'] > 279].index
    df.drop(clean_it , inplace=True)
    return df

def drop_50_pct_null(df):
    '''This function takes in the zillow df
    removes all columns and rows with 50% nulls or more
    returns df'''
    # Drop columns with 50% or more missing values
    df = df.dropna(axis = 1, thresh = 0.5 * len(df.index))
    # went from 67 columns down to 33
    # drop rows with 50% or more missing vlaues
    df.dropna(axis = 0, thresh = 0.5 * len(df.columns))
        # ended up not dropping any rows 
            # will remain in the function in case anything were to change later on
    return df