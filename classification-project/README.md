Data Dictonary
**senior_citizen** = senior or not senior(int - (0 or 1))
**partner**	= has partner or not-(int - (0 or 1))
**dependents** = has dependent or not-(int - (0 or 1))
**phone_service** = has a phone or not-(int - (0 or 1))
**tenure** = How long (in months) they have been with the company(float)
**multiple_lines** = has a multiple lines or not(int - (0 or 1))
**online_security**	= security or not (int - (0 or 1))
**online_backup** = backup or not (int - (0 or 1))
**device_protection** = protection or not (int - (0 or 1))
**tech_support** = support or not (int - (0 or 1))
**streaming_tv** = tv streaming or not (int - (0 or 1))
**streaming_movies** = movie stremaing or not (int - (0 or 1))
**paperless_billing** = paperless or not (int - (0 or 1))
**monthly_charges** = how much customers are charged each month (float)
**total_charges** = how much each customer has been charged through their tenure (float)
**churn** = churned or not (int - (0 or 1))
**contract_type** = are the month to month, one year, or two year customers (object)
**is_female** = are they female or not (int - (0 or 1))
**DSL** = Are the DSL customers or not (int - (0 or 1))
**fiber_optic** =  Are they fiber customers or not (int - (0 or 1))
**no_internet** =  Do they have internet or not (int - (0 or 1))
**bank_transfer** = Do they pay with bank transfers or not (int - (0 or 1))
**credit_card** = Do they pay with a credit card or not (int - (0 or 1))
**electronic_check** = Do they pay with electronic checks or not (int - (0 or 1))
**mailed_check** = Do they pay with mailed in checks or not (int - (0 or 1))


# Project Planning
 **Plan** -> Acquire -> Prepare -> Explore -> Model & Evaluate -> Deliver

- Project description:
    - By using what I have learned in the Classification Module:
        - data acquisition
        - data preparation
        - tidy data
        - exploratory analysis
        - evaluation
        - and modeling
            - I will be showing my code, findings, models, key takeaways, and recommendations regarding churn prediction.

- My goal is to:
    - find that major drivers of customer churn within the company
    - recreate a model that predicts churn accuratly
    - and create a clean report of all my work that is understandable by all.

- My deliverable:   
    - A clean, readable jupyter notebook report that include my cleaned up code, findings, models, key takeaways, and recommendations.

- Task out how you will work through the pipeline in as much detail as you need to keep on track.

    - Planning:
        - define the project itself in detail
        - define my ultimate goals of the project
        - how do I define succuess?
            - what is my deliverable?
                - how will I know I have succeeded?
        - how will I reach my goal?
            - how will i get from point a to point b
                - all the way down to when I give my presentation.
        - include my Data Dictionary
            - providing context of what is going to be used
            - explian my data
        - hypothesis 
            - these dont have to be your hard fast hypothesis.  
                - but I have looked at this data before when working on my story telling project. So I already have thought and mini hypothesis and those are what will be used in the planning stage.

    - Acquisition:
        - Create a path from my og data source to jupyter notebook so I can prepare and clean it.
            - In the acquire.py file (which has already been made)
                - store the proper imports to run all of the code
                - Create and store functions that needed to get the data from the telco chrun database.
                    - should return pandas data frame
        - determine the deliverable
            - the acquire file as stated up and the above bullet point.

    - Preparation:
        - In prepare.py store functions needed to prepare my data(important imports to run code)
            - The final function should be able to:
                - Split my data into train, validat, and test
                    - that can be explored, analyzed and visualized with ease.
                - Handle missing values
                - Handle incorrect data and outlier tht I may want to address.
                - Encode Variables
                - Create new features if wated
        - In my jupyter notebook
            - Clean my data
                - Explore missing values and document takeaways/action plans for handling them
                    - explain why I did what I did
                        - I dropped this column because ____________.
                        - I did this because of that
                    - is "missing" mean 0 or somehting else?
                    - should I replace any missing values with it most likely represents like mean, median, or mode?
                    - should i just remove the cariable column due to how much missing data there is?
                    - should I romove rows with missing data?
                - Explore data types and adapt types or data values as needed to have numeric represenations of each attribute
                    - are these data types correct?
                    - is it reading as an object when they are numeric?
                        - maybe one of the values has an object that is causing this issue?
            - Create any new features you want to use in your model. Some ideas you might want to explore after securing an MVP ( minimum viable product)
                - add a column to represent tenure but in years not months
                - single variables for or find other methods to merge variables representing the information from the following columns:
                    - phone_service and multiple_lines
                    - dependents and partner
                    - streaming_tv & streaming_movies
                    - online_security & online_backup
                - is there a minimum?

    - Exploration:
        - In my jupyter notebook:
            - Answers:
                - key questions
                - answer my hypothesis
                - determine the drivers of churn
                    - making sure to have at least 2 stat tests run
            - Makes sure to
                - Creating visualizations
                - Run statistical tests
                - Document findings based on stat tests ran
                    - the goal is to
                        - identify features that relate to churn
                        - indentify data integrity issues
                        - understand how my data works
                    - if there is a correlation
                        - assume there is no causal relationship and brainstorm (and document) ideas on reasons there could be correlation
            - Summarize my cnclusion, be able to answer question, and summarize takeaways and recomendations.

    - Modeling:
        - In my notebook:
            - Require to establish a baseline accuracy to determine if having a model is better than no model and train and compare at least 3 different models.
                - Each step documented VERY well
            - Train (fit, transform, evaluate) multiple models, varying the algorithm and/or hyperparameters you use.
            - Compare evaluation metrics across all the models you train and select the ones you want to evaluate using your validate dataframe.
            - Are there any variables that seem to provide limited to no additional information?
                - Yes?
                    - remove them
                - No?
                    - leave it be
            - Based on the evaluation choose the best model to test the data
            - Test the final model on my out of sample sata (the data set itself)
                - summarize , interpret, and document the results

    - Delivery:
        - Introduce myself
        - Introduce the project and goal
        - Summarize the findings (think of the Executive summary in a presenation)
        - The analysis I did to answer the questions and that lead to my findings. Relationships clearly visualized and takeaways are documented.
        - Finish with key takeaways, recommendations, and next steps and be prepared to answer questions from the data science team about your project.
        - Remember you have a time limit of 5 minutes for your presentation. Make sure you practice your notebook walkthrough keeping this time limit in mind; it will go by very quickly.

- Clearly state your starting hypotheses and add the testing of these to your task list.(going into it you already look at the data and did a project, state these thoguhts, they dont have to be formal hypothesis)
    - Higher Monthly Charges drive churn
    - Whether someone is single with no kids drives chrun
    - If someone has Fiber they are more likey to churn
    - If someone has a phone service they are more likely to stay.
    - Contracts of single people with no children, with the a month to month contract have extremely high churn.


--------------------------------------------------------------------------------------------------------------------------------------------------------------------

# Project Acquiring
 Plan -> **Acquire** -> Prepare -> Explore -> Model & Evaluate -> Deliver

Functions used can be found in acquire.py in git hub repo

1. acquire the get_churn_data as df
2. check out the .info
3. check out the .describe

--------------------------------------------------------------------------------------------------------------------------------------------------------------------

# Project Preperation
 Plan -> Acquire -> **Prepare** -> Explore -> Model & Evaluate -> Deliver

Functions used can be found in prepare.py in git hub repo

1. Clean the data:
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
                will remove payment_type_id, internet_service_type_id, contract_type_id, gender columns, contract_type, internet_service_type, 
                and payment_type
                rename internet_service_type_DSL to DSL
                rename internet_service_type_Fiber optic to fiber_optic
                rename internet_service_type_None to no_internet
                rename payment_type_Bank transfer (automatic) to bank_transfer
                rename payment_type_Credit card (automatic) to credit_card
                rename payment_type_Electronic check to electronic_check
                rename payment_type_Mailed check to mailed_check
                change columns to integer format instead of object or string: 'is_female', 'partner', 'dependents', 'phone_service', 'streaming_tv', 'streaming_movies', 'paperless_billing', 'churn', 'multiple_lines', 'online_security', 'online_backup', 'device_protections', 'tech_support', 'total_charges'
                return: a single pandas dataframe with the above operations performed
2. check out the new .info
3. check out the new .describe
4. check out the calue_counts
5. run a df.isna().sum()
    - returned 0
6. run a df.null().sum()
    -returned 0
7. split the data

--------------------------------------------------------------------------------------------------------------------------------------------------------------------

# Project Exploration
 Plan -> Acquire -> Prepare -> **Explore** -> Model & Evaluate -> Deliver

1. pull my acquire
2. pull my prepare and prepare_telco
3. split my data
4. create correlation heat map
        - In the above chart:
            - the darked the color the stronger the correlation is
            - the lighter the color the weaker the correlation is
        - The strongest correlations to churn are:
            - monthly charges
                - .2
            - tenure
                - -.35
            - fiber optic service
                - .31
            - electronic check payment
                - .3
            - no internet service
                - -.23
        - Monthly Charges:
            - Continuous
        - Tenure:
            - Continuous
        - Fiber optic
            - Categorical
        - Electronic check
            - Categorical
        - No internet Service
            - Categorical
5. Create histograms for features being used
6. Run a stat test for each feature
    - t test for categorical vs continuous
    - chi test for categorical vs categorical
7. Answering my questions:
    How much of churn is effected by high monthly charges?
        20%
    at what price is there a spike?
        70 per month
    does it go back down after the spike(if there is one)?
        at 110 per month the churn starts going back down
    Does tenure have high churn?
        yes
    How many fiber optic customers churn?
        905 of the 2170 fiber optic customers churn
            41.7% of the fiber optic customers churn

--------------------------------------------------------------------------------------------------------------------------------------------------------------------

# Project Modeling and Evaluation
 Plan -> Acquire -> Prepare -> Explore -> **Model & Evaluate** -> Deliver

1. Create prediction models with in sample data
    - baseline accuracy
        - 0.73
    - logit
        - .8
    - decision tree
        - .78
    - random forest
        - .78
    - knn
        - .79
2. Logit ran best with all 5 features
3. Run the Logit with out of sample
    - .8 accuracy 

--------------------------------------------------------------------------------------------------------------------------------------------------------------------

# Project Delivery
 Plan -> Acquire -> Prepare -> Explore -> Model & Evaluate -> **Deliver**