import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

df = pd.read_csv("student_depression_dataset.csv")


"""getting info about the data
and knowing anout the data"""
describe = df.describe()
print(describe)

info = df.info()
print(info)

hey = df.head()
print(hey)

'''grouping the data to understand the data'''



grouping = df.groupby("Gender" )["Age"].mean()

print(grouping)




'''grouping the members of different age groups'''


bins = [0,15,20,25,30,100]
labels = ["0-15","16-20" , "21-25" , "26-30" , "30+"]

df["Age_grouping"] = pd.cut(df["Age"],bins= bins ,labels = labels)

print(df["Age_grouping"].value_counts())
#output 21-25 more students are there
'''21-25    8573
26-30    7845
30+      6099
16-20    5384
0-15        0'''

know = df.groupby("Age_grouping") ["Depression"].mean() * 100


print(know)

'''Age_grouping
0-15           NaN
16-20    72.343982
21-25    64.294879
26-30    56.532823
30+      40.891949'''


def group_bydiff(df,group_call,value_call,xlabel,ylabel,title):
    df.groupby(group_call) [value_call].mean().plot(kind = "bar")

    plt.title(title)
    plt.xlabel(xlabel)
    plt.ylabel(ylabel)

    plt.show()

group_bydiff(df,"Age_grouping","Depression","age label","rate of depression","depresson analysis by age group")



group_bydiff(df,"Age_grouping",'Work Pressure',"Age Group", "Work Pressure" ,"work pressure analysis by age group")
                


group_bydiff(df,"Age_grouping",'Academic Pressure', "Age Group" ,"Academic Pressure","Academic Pressure analysis by age group")
                

group_bydiff(df,"Gender","Work Pressure","Gender","Work Pressure","Work Pressure analysis by Gender")




group_bydiff(df,"Age_grouping",'Study Satisfaction',"Age Group","Study satisfication", "study satisfication by age grouping")
                


