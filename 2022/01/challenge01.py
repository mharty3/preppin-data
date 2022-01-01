# https://preppindata.blogspot.com/2022/01/2022-week-1-prep-school-parental.html
# 2022-01-07

import pandas as pd
import numpy as np

# read input data
RAW = pd.read_csv(
    r"2022/01/inputs/PD 2022 Wk 1 Input - Input.csv", parse_dates=["Date of Birth"]
)

# create output df to store results
output = pd.DataFrame()

output["Pupil's Name"] = RAW["pupil last name"] + ", " + RAW["pupil first name"]

preferred_contact = RAW["Parental Contact Name_1"].where(
    RAW["Parental Contact"] == 1, RAW["Parental Contact Name_2"]
)

output["Parental Contact Full Name"] = RAW["pupil last name"] + ", " + preferred_contact

output["Parental Contact Email Address"] = (
    preferred_contact
    + "."
    + RAW["pupil last name"]
    + "@"
    + RAW["Preferred Contact Employer"]
    + ".com"
)

output["Academic Year"] = np.ceil(
    ((pd.to_datetime("2014-09-01") - RAW["Date of Birth"]).dt.days / 365.25) + 1
).astype(int)

output.to_csv(
    r"2022/01/outputs/output.csv",
    columns=[
        "Academic Year",
        "Pupil's Name",
        "Parental Contact Full Name",
        "Parental Contact Email Address",
    ],
)

# Input the csv file 
# Form the pupil's name correctly for the records in the format Last Name, First Name 
# Form the parental contact's name in the same format as the pupil's 
#     The Parental Contact Name 1 and 2 are the first names of each parent.
#     Use parental contact column to select which parent first name to use along with the pupil's last name
# Create the email address to contact the parent using the format Parent First Name.Parent Last Name@Employer.com
# Create the academic year the pupils are in 
#     Each academic year starts on 1st September.
#     Year 1 is anyone born after 1st Sept 2014 
#     Year 2 is anyone born between 1st Sept 2013 and 31st Aug 2014 etc
# Remove any unnecessary columns of data 
# Output the data 
