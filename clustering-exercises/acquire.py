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
    join (select parcelid, max(logerror) as logerror, max(transactiondate) as transactiondate
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
