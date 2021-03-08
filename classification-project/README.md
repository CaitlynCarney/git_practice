- Time Management:
    - Day 1 (Friday, 5th of March)
        - Finish Planning Stage
            - Completed
        - Finish the Acquire Stage
            - Completed
    - Day 2 ( Saturday, 6th of March)
        - Finish Prepare stage
            - 
        - Finsih Explore Stage
            - 
    - Day 3 (Sunday, 7th of March)
        - Finish MOdel and Evaluate Stage
            - 
        - Clean up Notebook
            - 
        - Start practicing delivery
            - 
    - Day 4 (Monday, 8th of March)
        - Practice
        - Practice
        - Practice
    - Day 5 (Tuesday, 9th of March)
        - Present

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



--------------------------------------------------------------------------------------------------------------------------------------------------------------------

# Project Preperation
 Plan -> Acquire -> **Prepare** -> Explore -> Model & Evaluate -> Deliver



--------------------------------------------------------------------------------------------------------------------------------------------------------------------

# Project Exploration
 Plan -> Acquire -> Prepare -> **Explore** -> Model & Evaluate -> Deliver




--------------------------------------------------------------------------------------------------------------------------------------------------------------------

# Project Modeling and Evaluation
 Plan -> Acquire -> Prepare -> Explore -> **Model & Evaluate** -> Deliver



--------------------------------------------------------------------------------------------------------------------------------------------------------------------

# Project Delivery
 Plan -> Acquire -> Prepare -> Explore -> Model & Evaluate -> **Deliver**