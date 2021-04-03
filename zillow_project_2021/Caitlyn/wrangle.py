import env
import pandas as pd

import sklearn.preprocessing
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import MinMaxScaler
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

def get_connection(db, user=env.user, host=env.host, password=env.password):
    
    return f'mysql+pymysql://{user}:{password}@{host}/{db}'
    
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# Acquire
def get_zillow_data():
    '''
    Grab our data from path and read as dataframe
    '''
    
    df = pd.read_sql('''
                        SELECT *
                        FROM   properties_2017 prop  
                               INNER JOIN (SELECT parcelid,
                                                  logerror,
                                                  Max(transactiondate) transactiondate 
                                           FROM   predictions_2017 
                                           GROUP  BY parcelid, logerror) pred
                                       USING (parcelid) 
                               LEFT JOIN airconditioningtype air USING (airconditioningtypeid) 
                               LEFT JOIN architecturalstyletype arch USING (architecturalstyletypeid) 
                               LEFT JOIN buildingclasstype build USING (buildingclasstypeid) 
                               LEFT JOIN heatingorsystemtype heat USING (heatingorsystemtypeid) 
                               LEFT JOIN propertylandusetype landuse USING (propertylandusetypeid) 
                               LEFT JOIN storytype story USING (storytypeid) 
                               LEFT JOIN typeconstructiontype construct USING (typeconstructiontypeid) 
                       WHERE transactiondate like '2017-%%-%%'
                               AND prop.latitude IS NOT NULL
                               AND prop.longitude IS NOT NULL
                               
                               AND propertylandusetypeid between 260 AND 266
                               OR propertylandusetypeid between 273 AND 279
                               AND NOT propertylandusetypeid = 274
                               AND unitcnt = 1;''', get_connection('zillow'))
    return df

#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

# Prepare

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

def clean_zillow(df):
    '''This function takes in the df
    applies all the cleaning funcitons previously created
    creates features
    drops columns
    renames columns'''
    # assuming null value for pool and fireplacecnt means none
    df.poolcnt.fillna(0, inplace = True)
    df.fireplacecnt.fillna(0, inplace = True)
    # drop features/rows with more than 50% null values
    df = drop_50_pct_null(df)
    # create dummy variables and add them to the df
    dummy_df =  pd.get_dummies(df['fips'])
    dummy_df.columns = ['in_los_angeles', 'in_orange_county', 'in_ventura']
    df = pd.concat([df, dummy_df], axis=1)
    df['fips'] = df.fips.replace('6,037.00', 6037)
    df['fips'] = df.fips.replace('6,059.00', 6059)
    df['fips'] = df.fips.replace('6,111.00', 6111)
    #create new feature house_age
    today = pd.to_datetime('today')
    df['house_age'] = today.year - df['yearbuilt']
    df['tax_rate'] = df.taxvaluedollarcnt / df.taxamount
    df['level_of_log_error'] = pd.qcut(df.logerror, q=5, labels=['L1', 'L2', 'L3', 'L4', 'L5'])
    df['acres'] = df.lotsizesquarefeet/43560
    #drop features
    df = df.drop(['propertycountylandusecode', 'propertyzoningdesc', 
                 'heatingorsystemdesc', 'transactiondate',
                  'finishedsquarefeet12', 'id', 'censustractandblock',
                 'rawcensustractandblock', 'calculatedbathnbr', 
                 'assessmentyear', 'propertylandusedesc'], axis=1)
    #rename features
    df = df.rename(columns={'heatingorsystemtypeid':'has_heating_system', 
                           'bathroomcnt':'bathrooms', 'bedroomcnt':'bedrooms', 
                           'buildingqualitytypeid':'quality',
                           'calculatedfinishedsquarefeet':'square_feet', 
                           'fullbathcnt':'full_bathrooms',
                           'lotsizesquarefeet':'lot_square_feet', 
                           'propertylandusetypeid':'land_type',
                           'regionidcity':'city', 'regionidcounty':'county',
                           'regionidzip':'zip_code', 'roomcnt':'room_count',
                           'structuretaxvaluedollarcnt':'structure_tax_value',
                           'taxvaluedollarcnt':'tax_value', 
                           'landtaxvaluedollarcnt':'land_tax_value', 
                           'fireplacecnt':'has_fireplace',
                           'poolcnt':'has_pool'})
    # assuming that null means no heating bc it is southern CA
    df.has_heating_system.fillna('13', inplace = True)
    # change has_heating_system to binary
    df['has_heating_system'] = df.has_heating_system.replace([2.0, 7.0, 24.0, 6.0, 20.0, 13.0, 18.0, 1.0, 10.0, 11.0], 1)
    df['has_heating_system'] = df.has_heating_system.replace('13', '0')
    df['has_heating_system'] = (df['has_heating_system'] == True ).astype(int)
    # all of these are 1 unit counts
    df.unitcnt.fillna(1, inplace = True)
    df['unitcnt'] = df.unitcnt.replace([2.0, 3.0, 4.0, 6.0], 1)
    # change has_fireplace to a binary
    df['has_fireplace'] = df.has_fireplace.replace([2.0, 3.0, 4.0, 5.0], 1)
    df['has_fireplace'] = df.has_fireplace.replace(0.0, 0)
    #fix has_pool to int
    df['has_pool'] = df.has_fireplace.replace(1.0, 1)
    df['has_pool'] = df.has_fireplace.replace(0.0, 0)
    # fix unitcnt to int
    df['unitcnt'] = (df['unitcnt'] == True ).astype(int)
    # replacing null in quality feature with its median range (6)
    df.quality.fillna(6.0, inplace = True)
    # replacing null in square_feet with its median
    df.lot_square_feet.fillna(7313, inplace = True)
     # replacing null in quality feature with its median
    df.square_feet.fillna(1511, inplace = True)
     # replacing null in quality feature with its median
    df.full_bathrooms.fillna(2, inplace = True)
     # replacing null in quality feature with its median
    df.yearbuilt.fillna(1970, inplace = True)
     # replacing null in quality feature with its median
    df.structure_tax_value.fillna(134871, inplace = True)
     # replacing null in quality feature with its median
    df.house_age.fillna(51, inplace = True)
     # replacing null in quality feature with its median
    df.city.fillna(25218, inplace = True)
     # replacing null in quality feature with its median
    df.zip_code.fillna(96410, inplace = True)
    #drop remaining null values
    df = df.dropna()
    # change la, oc, and vent into int
    df['in_los_angeles'] = (df['in_los_angeles'] == True ).astype(int)
    df['in_orange_county'] = (df['in_orange_county'] == True ).astype(int)
    df['in_ventura'] = (df['in_ventura'] == True ).astype(int)
    # set index as parcelid
    df = df.set_index('parcelid')
    # finish dropping
    df = df.drop(['Unnamed: 0', 'yearbuilt'], axis=1)
    # Handle outliers
    df = df[df.tax_value < 1153326.5]
    df = df[df.square_feet < 4506.0]
    df = df[df.acres < 0.665426997245179]
    # bin some of the large features
    # bin the square feet
    df['square_feet_bins'] = pd.cut(df.square_feet, 
                            bins = [0,500,1000,1500,2000,2500,3000,3500,4000,4600],
                            labels = [1, 2, 3, 4, 5, 6, 7, 8,9])
    df['square_feet_bins'] = (df['square_feet_bins']).astype(int)
    # bin lot square feet
    df['lot_sqft_bins'] = pd.cut(df.lot_square_feet, 
                            bins = [0,10000,20000,30000,40000,50000,60000,70000,10000000],
                            labels = [0, 1, 2, 3, 4, 5, 6, 7])
    df['lot_sqft_bins'] = (df['lot_sqft_bins']).astype(int)
    # bin acres
    df['acre_bins'] = pd.cut(df.acres, 
                            bins = [0,25,50,75,100,125,150,175],
                            labels = [0, 1, 2, 3, 4, 5, 6])
    df['acre_bins'] = (df['acre_bins']).astype(int)
    return df

#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

# Split the Data into Tain, Test, and Validate.

def split_zillow(df):
    '''This fuction takes in a df 
    splits into train, test, validate
    return: three pandas dataframes: train, validate, test
    '''
    # split the focused zillow data
    train_validate, test = train_test_split(df, test_size=.2, random_state=1234)
    train, validate = train_test_split(train_validate, test_size=.3, 
                                       random_state=1234)
    return train, validate, test


# Split the data into X_train, y_train, X_vlaidate, y_validate, X_train, and y_train

def split_train_validate_test(train, validate, test):
    ''' This function takes in train, validate and test
    splits them into X and y versions
    returns X_train, X_validate, X_test, y_train, y_validate, y_test'''
    X_train = train.drop(columns = ['logerror'])
    y_train = train.logerror
    X_validate = validate.drop(columns=['logerror'])
    y_validate = validate.logerror
    X_test = test.drop(columns=['logerror'])
    y_test = test.logerror
    return X_train, X_validate, X_test, y_train, y_validate, y_test

#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

# Scale the Data


def scale_my_data(train, validate, test):
    scale_columns = ['bathrooms', 'bedrooms', 'quality', 
              'square_feet', 'full_bathrooms', 
              'latitude', 'longitude', 'lot_square_feet',  
              'land_type', 'city', 'county', 'zip_code', 
             'room_count', 'unitcnt', 'structure_tax_value', 
             'tax_value',  'land_tax_value', 'taxamount',
              'house_age', 'tax_rate', 'acres']
    scaler = MinMaxScaler()
    scaler.fit(train[scale_columns])

    train_scaled = scaler.transform(train[scale_columns])
    validate_scaled = scaler.transform(validate[scale_columns])
    test_scaled = scaler.transform(test[scale_columns])
    #turn into dataframe
    train_scaled = pd.DataFrame(train_scaled)
    validate_scaled = pd.DataFrame(validate_scaled)
    test_scaled = pd.DataFrame(test_scaled)
    
    return train_scaled, validate_scaled, test_scaled
