import pandas as pd
import numpy as np

df = pd.read_csv("adult.data.csv")

#Function to find the race and the number of people belong to that race from data
def race_series():
    count_white=(df["race"]=="White").sum()
    count_black=(df["race"]=="Black").sum()
    count_Asian_Pac_Islander=(df["race"]=="Asian-Pac-Islander").sum()
    count_Amer_Indian_Eskimo=(df["race"]=="Amer-Indian-Eskimo").sum()
    other_race=(df["race"]=="Other").sum()
    name_races=["White","Black","Asian_Pac_Islander","Amer_Indian_Eskimo","Other"]
    num_races=(count_white,count_black,count_Asian_Pac_Islander,count_Amer_Indian_Eskimo,other_race)
    series=pd.Series(num_races,index=name_races)
    return (series)

# Function to find the average age of the mens in data
def average_mean():
    means=df.loc[(df["sex"]=="Male"),"age"].mean()
    return (round(means,2))


#Find percent of people who have Bachelors degree  in education from data
def education_bachelors():
    total_edu=len(df["education"])
    bachelor_edu=(df["education"]=="Bachelors").sum()
    percent=round(((bachelor_edu/total_edu)*100),2)
    
    return f"{percent}%"

#Finding the percent of people which have advanced degree and salary is above 50k
def salary_above_ad():
    num_people_ad = df["education"].isin(["Bachelors", "Masters", "Doctorate"]).sum()
    
    num_people_above50=((df["education"].isin(["Bachelors", "Masters", "Doctorate"]))&(df["salary"].str.upper()==">50K")).sum()
    percent = round((num_people_above50/num_people_ad)*100,2)
    
    return f"{percent}%"


#Finding the percent of people which do not have advanced degree and salary is above 50k
def salary_above_non_ad():
    
    num_people_above50=(~(df["education"].isin(["Bachelors", "Masters", "Doctorate"]))&(df["salary"].str.upper()==">50K")).sum()
    num_people=(~(df["education"].isin(["Bachelors", "Masters", "Doctorate"]))).sum()
    percent=round((num_people_above50/num_people)*100,2)
    
    return f"{percent}%"


#Function to find the minimun hour to work
def min_hour():
    return df["hours-per-week"].min()

#Function to find the percent of people who has least hour and salary more than 50K
def min_and_above():
    num_hour_min=(df["hours-per-week"]==(df["hours-per-week"]).min()).sum()
    salary_above_1=((df["hours-per-week"]==(df["hours-per-week"]).min()) & (df["salary"].str.upper()==">50K")).sum()
    percent=round((salary_above_1/num_hour_min)*100,2)
    return f"{percent}%"


def high():
    num_earner=df["native-country"].value_counts()
    num_high_earner=df[df["salary"] == ">50K"]["native-country"].value_counts()
    percent=((num_high_earner/num_earner)*100).fillna(0)
    highest_earn=percent.idxmax()
    return (highest_earn,float(percent.max()))

#Function to find the most popular salary in india with more than 50K salary
def occu():
    occupation = df[(df["salary"] == ">50K")&(df["native-country"]=="India")]['occupation'].value_counts().idxmax()
    return occupation

print(race_series())
print(average_mean())
print(education_bachelors())
print(salary_above_ad())
print(salary_above_non_ad())
print(min_hour())
print(min_and_above())
print(high())
print(occu())