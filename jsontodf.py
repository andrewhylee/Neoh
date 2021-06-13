# Import Libraries
import json
import pandas as pd
import numpy as np
import os

today_date = "5_22"

# ----- PART 1: Get Matrix Data into Dataframe
with open (f"CleanedClassesFromMatrix{today_date}.json", "r") as myfile:
    data = json.load(myfile)
df_m = pd.DataFrame(data["classes"])


# ----- PART 2: Get Genius Data into Dataframe
df_g = pd.read_csv(f"ClassesFromGenius{today_date}.csv")


# ----- PART 3: Genius Dataframe Modifications
def put_name_in_first_last_order(name):
    proper_name = " ".join(reversed(name.split(', ')) )
    return proper_name

def get_rid_of_template(className):
    className_list = className.split(' ')
    for idx, word in enumerate(className_list):
        if word == "(Template)" : className_list.remove(word)
        if word == "(UbD" : 
            className_list.remove(word)
            className_list.remove(className_list[idx])
        # if word == "Template)" : className_list.remove(word)
    return " ".join(className_list)

df_g["studentName"] = df_g["studentName"].apply(put_name_in_first_last_order)
df_g["teacherName"] = df_g["teacherName"].apply(put_name_in_first_last_order)
df_g["className"] = df_g["className"].apply(get_rid_of_template)
df_g = df_g.loc[df_g["className"] != "Buzz Orientation for Students"]
df_g = df_g.loc[df_g["className"] != "Virtual Orientation for Students"]
df_g = df_g.loc[df_g["studentName"] != "Student, Test"]
df_g["className"] = df_g["className"].apply(lambda s: s.split(" ", 1)[1] if s[0].isdigit() else s)
df_g.reset_index(inplace=True, drop=True)


# ----- PART 4: Matrix Dataframe Modifications
matrix_className_conv_entire = {
    "Executive Functioning/Organizational Skills" : "TM",
    
    "English Elective A" : "English Elective",
    "History Elective A" : "History Elective",
    "Math Elective A" : "Math Elective",
    "Art Elective A" : "Art Elective",
    "Music Elective A" : "Music Elective",

    # "Art Elective B" : "Art Elective Semester 2",
    # "Art Elective Semester 2" : "Art Elective",
    "Art Elective B" : "Art Elective",
    "Music Elective B" : "Music Elective",
}

matrix_className_conv = {
    "Semester 2" : "B", 
    "Semester 1": "A",
    'Prec' : 'Pre-C',
    'Prea' : 'Pre-A',
    'Pre Alg' : 'Pre-Alg',
    "Middle School Elective" : "Middle School Elective Course",
    "United States" : "US",
    "High School Elective" : "Elective Course", 
    "Anatomy & Physiology" : "Anatomy and Physiology",
    "Integrated Chemistry & Physics" : "Integrated Science Physics and Chemistry",
    "American Sign Language" : "ASL",
    #"Middle School" : "MS",
}

matrix_className_conv_2 = {
    "Music 6" : "Music",
}

matrix_studentName_conv = {
    'GABE' : 'Gabriel',
    'Leo' : 'Leonardo',
    'Tom' : 'Junqi',
    'Drew Ston' : 'Fiona Ston',
    'Aaron Rosenber' : 'Yitzchak Rosenber',
    "El Fortea-Torrell" : "Eliane Fortea-Torrell",
    "Aj Kudle" : "Alec Kudle",
    "Nico Zonc" : "Nicola Zonc",
    "Leo Esposit" : "Leo Esposit",
    "Leo" : "PLACEHOLDER", # Something freaky is going on with this
    "Lake Wasserma" : "Liron Wasserma",
    "Archie Bomme" : "Archer Bomme",
    "Alexa Brandmeye" : "Alexandra Brandmeye",
    "Lilly-June Gordo" : "Lilly Gordo",
    "Zach Cohn" : "Zachary Cohn",
    "Mike Mandell" : "Michael Mandell",
    "Leah Esther Ostroff" : "Leah Ostroff",
    "Quino Nevares" : "Joaquin Nevares",
    "Ben Barth" : "Benjamin Barth",
}

matrix_studentName_conv_entire = {
    "PLACEHOLDER DeNiro" : "Leandro DeNiro", #Wrongly Spelled in Genius
    "PLACEHOLDER Esposito" : "Leo Esposito",
}



df_m["className"] = df_m["className"].replace(matrix_className_conv, regex=True)
df_m["className"] = df_m["className"].replace(matrix_className_conv_entire)
df_m["className"] = df_m["className"].replace(matrix_className_conv_2, regex=True)
df_m["studentName"] = df_m["studentName"].replace(matrix_studentName_conv, regex=True)
df_m["studentName"] = df_m["studentName"].replace(matrix_studentName_conv_entire)
classes_no_need_ms_prefix = {"English", "Language", "MS", "Middle"}
for i in range(df_m.shape[0]):
  cond1 = df_m["curriculumLevel"][i] == "Middle School"
  cond2 = df_m["curriculumLevel"][i] == "Honors"
  cond3 = df_m["className"][i].split(" ", 1)[0] not in classes_no_need_ms_prefix
  if cond1 and cond3:
    df_m["className"][i] = "MS " + df_m["className"][i]
  elif cond2:
    df_m["className"][i] = df_m["className"][i][:-1] + "Honors " + df_m["className"][i][-1:]
df_m.drop(columns=["sessionCount","sessionNumber","curriculumLevel"], inplace=True)



# ----- PART 5: Create Merged Dataframe
df_merged = df_m.merge(df_g, how = 'outer' ,indicator=True)
df_merged = df_merged.loc[df_merged["_merge"] == "left_only"]
df_merged.reset_index(inplace=True, drop=True)

# ----- PART 5.1: Drop Edge Cases from Merged Dataframe
edge_case_rows_indexes = []
edge_case_rows_indexes.append(*df_merged[ (df_merged["className"] == "TM") & (df_merged["studentName"] == "Meredith Moy") & (df_merged["teacherName"] == "Kenneth Eisner") ].index.values)
edge_case_rows_indexes.append(*df_merged[ (df_merged["className"] == "Post Secondary Planning Package") & (df_merged["studentName"] == "Zoe Siller") & (df_merged["teacherName"] == "Samantha Delgiudice") ].index.values)
edge_case_rows_indexes.append(*df_merged[ (df_merged["className"] == "Art Elective") & (df_merged["studentName"] == "Gunner Momsen") & (df_merged["teacherName"] == "Willa Rudolph") ].index.values)

# ------ Currently Being Subbed
edge_case_rows_indexes = [*edge_case_rows_indexes, *df_merged[ (df_merged["teacherName"] == "Gabrielle Legendre") ].index.values]

df_merged.drop(edge_case_rows_indexes, inplace=True)

# print(df_merged)
# df_mi = df.merge(df2, how = 'inner' ,indicator=True)
# print(df_m)

# ----- PART 6: Debugging Merge
# field = "studentName"
# value = "Abigail Davie"
# print(df_g.loc[df_g[field] == value])
# print(df_m.loc[df_m[field] == value])
# print(df_merged.loc[df_merged[field] == value])

print(df_g)
print(df_m)
print(df_merged)
print(edge_case_rows_indexes)

