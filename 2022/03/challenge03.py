#%%
# https://preppindata.blogspot.com/2022/01/2022-week-3-prep-school-passing-grades.html
# 2022-01-19
# wget --no-check-certificate 'https://docs.google.com/uc?export=download&id=1T1hQjAsedqtxFHD8Y9zwZ8Ohct3sPx_w' -O 2022/03/inputs/input1.csv                                                                   (base) 
# wget --no-check-certificate 'https://docs.google.com/uc?export=download&id=135o1Kj9koWM5eZ4VJjH9EUCyo1UnP54C' -O 2022/03/inputs/grades.csv             

import pandas as pd
import numpy as np

input1_raw = pd.read_csv('2022/03/inputs/input1.csv')
grades_raw = pd.read_csv('2022/03/inputs/grades.csv')

df = pd.DataFrame()
df = (input1_raw
        .join(grades_raw.set_index('Student ID'), on='id')
        .drop(columns=['pupil first name', 
                       'pupil last name',  
                       'Date of Birth',
                       'Parental Contact Name_1', 
                       'Parental Contact Name_2',
                       'Preferred Contact Employer', 
                       'Parental Contact'])
        .melt(id_vars=['id', 'gender'],
              var_name='Subject',
              value_name='Score')
        .assign(passed=lambda df_: df_['Score'] >= 75)
        .groupby('id')
        .agg(passed_subjects=('passed', 'sum'),
             students_avg_score=('Score', 'mean'),
             gender=('gender', 'first')
            )
        .reset_index()
        .round(1)
        .rename(columns={'id': 'Student ID',
                         'passed_subjects': 'Passed Subjects',
                         'students_avg_score': "Student's Avg Score",
                         'gender': 'Gender'})
).to_csv('2022/03/outputs/output.csv',
         columns=['Passed Subjects', 
                  "Student's Avg Score", 
                  'Student ID', 
                  'Gender'],
                  index=False)

# %%
