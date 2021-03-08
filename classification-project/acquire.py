import pandas as pd
import numpy as np
import os
from env import host, user, password

###################### Acquire Titanic Data ######################

def get_connection(db, user=user, host=host, password=password):
    '''
    This function uses my info from my env file to
    create a connection url to access the Codeup db.
    '''
    return f'mysql+pymysql://{user}:{password}@{host}/{db}'
    
    
    
def new_churn_data():
    '''
    This function reads the telco_churn data from the Codeup db into a df,
    write it to a csv file, and returns the df.
    '''
    # Create SQL query.
    sql_query = '''select *
    from customers
    join contract_types using(contract_type_id)
    join internet_service_types using(internet_service_type_id)
    join payment_types using(payment_type_id)'''
    # Read in DataFrame from Codeup db.
    df = pd.read_sql(sql_query, get_connection('telco_churn'))
    return df



def get_churn_data(cached=False):
    '''
    This function reads in telco_chrun data from Codeup database and writes data to
    a csv file if cached == False or if cached == True reads in telco_churn df from
    a csv file, returns df.
    '''
    if cached == False or os.path.isfile('telco_churn.csv') == False:
        # Read fresh data from db into a DataFrame.
        df = new_churn_data()
        # Write DataFrame to a csv file.
        df.to_csv('telco_churn_df.csv')
    else:
        # If csv file exists or cached == True, read in data from csv file.
        df = pd.read_csv('telco_churn_df.csv', index_col=0)
    return df