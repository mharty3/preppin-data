# https://preppindata.blogspot.com/2022/01/2022-week-2-prep-school-birthday-cakes.html
# 2022-01-12
import pandas as pd
import numpy as np

# read input data. same input as week 1
RAW = pd.read_csv(
    r"2022/01/inputs/PD 2022 Wk 1 Input - Input.csv", parse_dates=["Date of Birth"]
)


def prep_cake_day(RAW):
    df = pd.DataFrame()
    return df.assign(
        pupil_name=RAW["pupil first name"] + " " + RAW["pupil last name"],
        this_years_birthday=RAW["Date of Birth"] + pd.DateOffset(year=2022),
        month=RAW["Date of Birth"].dt.month_name(),
        weekday=lambda df_: df_["this_years_birthday"].dt.day_name(),
        # if the birthday is a weekend, we need cake on friday
        cake_needed_on=lambda df_: df_["weekday"].where(
            ~df_["weekday"].isin(["Saturday", "Sunday"]), "Friday"
        ),
        bds_per_weekday_and_month=lambda df_: df_.groupby(["month", "cake_needed_on"])[
            "pupil_name"
        ].transform("count"),
    ).drop(columns=["weekday"])


prep_cake_day(RAW).to_csv("2022/02/outputs/output.csv")
