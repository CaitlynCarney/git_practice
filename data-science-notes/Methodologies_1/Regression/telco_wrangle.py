def acquire_grades():
    '''
    Grab our data from a path and rea in from csv.
    '''
    df = pd.read_csv("student_grades.csv")
    return df

def clean_grades(df):
    '''
    Takes in df of students grades and cleans the data by
    droping null values
    replacing whitespace
    converting data to numerical data types
    dropping 'student_id' column
    
    returns a clean df as a pandas df
    '''
    # convert the white space in exam3 into a null value
    df['exam3'] = df['exam3'].replace(r'^\s*$', np.nan, regex = True)
    # Because we have evidence that these are missing grades in the df, we will not impute the values and deip the two rows that involve missing grades
    df = df.dropna()
    # switch it all to integer
    df = df.dropna().astype('int')
    # dropping student_id
    df = df.drop(columns = 'student_id')
    return df

def split_data(df):
    '''
    split our data
    takes in a pandas dataframe
    returns 3 panda dataframs:
        train
        test
        validate
    '''
    train_val, test = train_test_split(df, train_size=0.8, random_state=1234)
    train, validate = train_test_split(train_val, train_size=0.7, random_state=1234)
    return train, validate, test

def wrangle_grades():
    '''
    rangle_grades will read in our student grades as a pandas dataframe
    clean the date
    split the date
    return train, validate, test sets of pandas dataframe from students grades
    stratified on final_grade
    '''
    df = clean_grades(acquire_grades())
    return split_data(df)