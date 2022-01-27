#%%
# https://preppindata.blogspot.com/2022/01/2022-week-4-prep-school-travel-plans.html
# 2022-01-26

import pandas as pd

RAW = pd.read_csv('2022/04/inputs/travel_plans.csv')

MISTAKES = {
    'Scoter': 'Scooter',
    'Walkk': 'Walk',
    'Carr': 'Car',
    'Bycycle': 'Bicycle',
    'Scootr': 'Scooter',
    'Wallk': 'Walk',
    'WAlk': 'Walk',
    'Waalk': 'Walk',
    'Helicopeter': 'Helicopter' 
}

SUSTAINABILITY = {
    'Car': 'Non-Sustainable',
    'Bicycle': 'Sustainable',
    'Scooter': 'Sustainable',
    'Walk': 'Sustainable',
    'Aeroplane': 'Non-Sustainable',
    'Helicopter': 'Non-Sustainable',
    'Van': 'Non-Sustainable',
    "Mum's Shoulders": 'Sustainable',
    'Hopped': 'Sustainable',
    "Dad's Shoulders": 'Sustainable',
    'Skipped': 'Sustainable',
    'Jumped': 'Sustainable',
    'Helicopter': 'Non-Sustainable'
}

trip_counts_per_day = (RAW
                        .drop(columns=['Student ID'])
                        .count()
                        .rename('trips_per_day')
                       )

output = (RAW
        .melt(id_vars='Student ID', value_name='method', var_name='day')
        .assign(method = lambda df_: (df_['method']
                                        .map(MISTAKES)
                                        .fillna(df_['method'])),
                )
        .groupby(['day', 'method'])['Student ID']
        .count()
        .reset_index()
        .rename(columns={'Student ID': 'number_of_trips'})
        .join(trip_counts_per_day, on='day')
        .assign(
            sustainable=lambda df_: df_['method'].map(SUSTAINABILITY),
            percent_trips_per_day=lambda df_: df_['number_of_trips'] / df_['trips_per_day']
        )
        .round(2)
        .rename(columns={'sustainable': 'Sustainable?',
                         'method': 'Method of Travel',
                         'day': 'Weekday',
                         'number_of_trips': 'Number of Trips',
                         'trips_per_day': 'Trips per day',
                         'percent_trips_per_day': '% of trips per day'})
    
    ).to_csv('2022/04/outputs/output.csv',
        columns=['Sustainable?', 'Method of Travel', 'Weekday', 
                 'Number of Trips', 'Trips per day', '% of trips per day'],
        index=False)

