#!/usr/bin/env python3

import json
import pandas as pd
import csv
with open("raw_survey_data.csv", 'w', newline='') as csvfile:
    fieldnames = ['student_id','major','GPA','is_cs_major','credits_taken']
    cw = csv.DictWriter(csvfile,fieldnames=fieldnames)

    cw.writeheader();
    cw.writerow({'student_id': 3628361, 'major': "Cognitive Science", 'GPA' : 3.9, 'is_cs_major': 'No', 'credits_taken': '72.3'})
    cw.writerow({'student_id': 2734936, 'major': "Systems Engineering", 'GPA' : 3, 'is_cs_major': 'No', 'credits_taken': '85.0'})
    cw.writerow({'student_id': 4628462, 'major': "Computer Science", 'GPA' : 3.7, 'is_cs_major': 'Yes', 'credits_taken': '103.4'})
    cw.writerow({'student_id': 5836497, 'major': "Computer Science", 'GPA' : 4, 'is_cs_major': 'Yes', 'credits_taken': '115.2'})
    cw.writerow({'student_id': 4628462, 'major': "Data Science", 'GPA' : 3.8, 'is_cs_major': 'No', 'credits_taken': '48.8'})

json_d =  [{
            "course_id": "DS2002",
            "section": "001",
            "title": "Data Science Systems",
            "level": 200,
            "instructors": [
            {"name": "Austin Rivera", "role": "Primary"}, 
            {"name": "Heywood Williams-Tracy", "role": "TA"} 
            ]
        },
        {
            "course_id": "CS4774",
            "title": "Machine Learning",
            "level": 400,
            "instructors": [
            {"name": "Hadi Daneshmand", "role": "Primary"}
            ]
        },
        {
            "course_id": "CS3130",
            "section": "102",
            "title": "Computer Systems and Organization 2",
            "level": 300,
            "instructors": [
            {"name": "Kevin Skadron", "role": "Primary"}
            ]
        },
        {
            "course_id": "DS2004",
            "section": "001",
            "title": "Data Ethics",
            "level": 200,
            "instructors": [
            {"name": "Emmanuel Moss", "role": "Primary"}
            ]
        },
        {
            "course_id": "RELH2090",
            "title": "Hinduism",
            "level": 200,
            "instructors": [
            {"name": "Matthew Leveille", "role": "Primary"}
            ]
        }
        
        ]
with open("raw_course_catalog.json",'w',newline='') as jsonfile:
    json.dump(json_d,jsonfile,indent=2)
    

dataframe = pd.read_csv("raw_survey_data.csv")
dataframe['is_cs_major'] = dataframe['is_cs_major'].apply(lambda x: x == "Yes")
dataframe.astype({'GPA':'float64'})
dataframe.astype({'credits_taken':'float64'})

with open("cleaned_survey_data.csv",'w',newline='') as cleanfile:
    dataframe.to_csv(cleanfile)

with open("raw_course_catalog.json",'r') as j:
    data = json.load(j)

df = pd.json_normalize(data, record_path=['instructors'], meta=['course_id','title','level'])

with open("clean_course_catalog.csv", 'w',newline='') as json_to_csv:
    df.to_csv(json_to_csv)