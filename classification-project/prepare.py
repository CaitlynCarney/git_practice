import pandas as pd
from sklearn.model_selection import train_test_split

def clean_telco(df):
    '''
    clean_telco will take one argument df, a pandas dataframe, anticipated to be the telco_churn dataset
    change column form bool to interger where 0 stands for no/false and 1 stands for yes/true:
        'is_female'
        'partner'
        'dependents'
        'phone_service'
        'streaming_tv'
        'streaming_movies'
        'paperless_billing'
        'churn'
        'multiple_lines'
        'online_security'
        'online_backup'
        'online_protection'
        'tech_support'
    encode internet_service_type, payment_type into seperate new columns and add them to the df
    will remove payment_type_id, internet_service_type_id, contract_type_id, customer_id, gender columns, contract_type, internet_service_type, 
    and payment_type
    rename internet_service_type_DSL to DSL
    rename internet_service_type_Fiber optic to fiber_optic
    rename internet_service_type_None to no_internet
    rename payment_type_Bank transfer (automatic) to bank_transfer
    rename payment_type_Credit card (automatic) to credit_card
    rename payment_type_Electronic check to electronic_check
    rename payment_type_Mailed check to mailed_check
    add new columns: 'single_no_kids
    change columns to integer format instead of object or string: 'is_female', 'partner', 'dependents', 'phone_service', 'streaming_tv', 'streaming_movies', 'paperless_billing', 'churn', 'multiple_lines', 'online_security', 'online_backup', 'device_protections', 'tech_support', 'total_charges'
    return: a single pandas dataframe with the above operations performed
    '''
    dummy_df = pd.get_dummies(df[["internet_service_type", "payment_type"]], drop_first=False)
    df = pd.concat([df, dummy_df], axis=1)
    df['single_no_dep'] = (df['partner'] + df['dependents']).apply(lambda x: 1 if x == 0 else 0)
    df['no_streaming'] = (df['streaming_tv'] + df['streaming_movies']).apply(lambda x: 1 if x == 0 else 0)
    df['tenure_grouped'] = pd.cut(df.tenure, bins = [0, 20, 40, 60, 80], labels=['1-20', '20-40', '40-60', '60-80'])
    df["is_female"] = df.gender == "Female"
    df['is_female'] = (df['is_female'] == True ).astype(int)
    df["partner"] = df.partner == "Yes"
    df['partner'] = (df['partner'] == True ).astype(int)
    df["dependents"] = df.dependents == "Yes"
    df['dependents'] = (df['dependents'] == True ).astype(int)
    df["phone_service"] = df.phone_service == "Yes"
    df['phone_service'] = (df['phone_service'] == True ).astype(int)
    df["streaming_tv"] = df.streaming_tv == "Yes"
    df['streaming_tv'] = (df['streaming_tv'] == True ).astype(int)
    df["streaming_movies"] = df.streaming_movies == "Yes"
    df['streaming_movies'] = (df['streaming_movies'] == True ).astype(int)
    df["paperless_billing"] = df.paperless_billing == "Yes"
    df['paperless_billing'] = (df['paperless_billing'] == True ).astype(int)
    df["churn"] = df.churn == "Yes"
    df['churn'] = (df['churn'] == True ).astype(int)
    df["multiple_lines"] = df.multiple_lines == "Yes"
    df['multiple_lines'] = (df['multiple_lines'] == True ).astype(int)
    df["online_security"] = df.online_security == "Yes"
    df['online_security'] = (df['online_security'] == True ).astype(int)
    df["online_backup"] = df.online_backup == "Yes"
    df['online_backup'] = (df['online_backup'] == True ).astype(int)
    df["device_protection"] = df.device_protection == "Yes"
    df['device_protection'] = (df['device_protection'] == True ).astype(int)
    df["tech_support"] = df.tech_support == "Yes"
    df['tech_support'] = (df['tech_support'] == True ).astype(int)
    df = df.drop(["payment_type_id", 'internet_service_type_id', 'contract_type_id', 'customer_id', 'gender', "contract_type", 'internet_service_type', 'payment_type'], axis=1)
    df = df.rename(columns={'internet_service_type_DSL': 'DSL', 
                       'internet_service_type_Fiber optic': 'fiber_optic', 
                       'internet_service_type_None': 'no_internet', 
                       'payment_type_Bank transfer (automatic)': 'bank_transfer', 
                       'payment_type_Credit card (automatic)': 'credit_card', 
                       'payment_type_Electronic check': 'electronic_check', 
                       'payment_type_Mailed check': 'mailed_check'})
    df.total_charges = df.total_charges.str.strip()
    df = df[df.total_charges != ""]
    df['total_charges'] = df.total_charges.replace("'", '')
    df['total_charges'] = df.total_charges.replace(" ", "")
    df['total_charges'] = df.total_charges.replace(",", "")
    df['total_charges'] = df.total_charges.astype(float)
    
    return df


def prep_telco(df):
    '''
    prep_telco will take one argument df, a pandas dataframe, anticipated to be the telco_churn dataset
    and will remove payment_type_id, internet_service_type_id, contract_type_id, customer_id, gender columns, internet_service_type, 
    and payment_type
    rename internet_service_type_DSL to internet_service_type_DSL
    rename internet_service_type_Fiber optic to internet_service_type_fiber_optic
    rename internet_service_type_None to internet_service_type_none
    rename payment_type_Bank transfer (automatic) to payment_type_bank_transfer
    rename payment_type_Credit card (automatic) to payment_type_credit_card
    rename payment_type_Electronic check to payment_type_electronic_check
    rename payment_type_Mailed check to payment_type_mailed_check
    perform a train, validate, test split
    
    return: three pandas dataframes: train, validate, test
    '''
    
    df = clean_telco(df)
    train_validate, test = train_test_split(df, test_size=0.2, random_state=1349, stratify=df.churn)
    train, validate = train_test_split(train_validate, train_size=0.7, random_state=1349, stratify=train_validate.churn)
    return train, validate, test

def split(df, stratify_by=None):
    """
    Crude train, validate, test split
    To stratify, send in a column name
    """
    if stratify_by == None:
        train, test = train_test_split(df, test_size=.3, random_state=123)
        train, validate = train_test_split(df, test_size=.3, random_state=123)
    else:
        train, test = train_test_split(df, test_size=.2, random_state=123, stratify=df[stratify_by])
        train, validate = train_test_split(df, test_size=.3, random_state=123, stratify=train[stratify_by])
    return train, validate, test

from pandas import DataFrame
from sklearn.preprocessing import LabelEncoder
from sklearn.model_selection import train_test_split

#there are no missing values to handle according to my research

def train_validate_test_split(df, seed=123):
    train_and_validate, test = train_test_split(
        df, test_size=0.2, random_state=seed, stratify=df.churn
    )
    train, validate = train_test_split(
        train_and_validate,
        test_size=0.3,
        random_state=seed,
        stratify=train_and_validate.churn,
    )
    return train, validate, test