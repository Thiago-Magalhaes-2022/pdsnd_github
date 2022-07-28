"""Bikeshare Project"""
import pandas as pd
import time
from datetime import date, datetime

now_a = datetime.now()

CITY_DATA = { 'chicago': 'chicago.csv',
              'new york city': 'new_york_city.csv',
              'washington': 'washington.csv' }

print('Welcome! \n\nLet\'s explore some US bikeshare data!')

city = input("\nWhat city are you searching data about? \n\nChicago, New York City or Washington? ")

city = city.lower()

while (city.lower() not in ['washington', 'new york city', 'chicago']):
    city = input("\nIt was not possible to recognize the name of the city.\n\nPlease type again: \n")

city = city.lower()

month = input("\nWhat month are you searching data about? (Please type: January, February, March, April, May or June) ")

month = month.lower()

while (month.lower() not in ['january', 'february', 'march', 'april', 'may', 'june']):
    month = input("\nIt was not possible to recognize the month.\n\nPlease type again: \n")


day_info = input("\nWhat week day are you searching data about? (Please write as a number: Mon=1, Tue=2, Wed=3, Thu=4, Fri=5, Sat=6, Sun=7)  ")

day = day_info.lower()

while (day.lower() not in ['1', '2', '3', '4', '5', '6', '7']):
    day = input("\nIt was not possible to recognize the number of the weekday.\n\nPlease type again: \n")


"""Load data file into a dataframe"""
df = pd.read_csv(CITY_DATA[city])


"""Convert the Start Time column to datetime"""
df['Start Time'] = pd.to_datetime(df['Start Time'])


"""Extract month and day of week from Start Time to create new columns"""
df['month'] = df['Start Time'].dt.month
df['day_of_week'] = df['Start Time'].dt.weekday_name

"""By month if applicable"""
if month != 'all':
    months = ['january', 'february', 'march', 'april', 'may', 'june']
    month = months.index(month)+1

    df = df[df['month'] == month]


if day != 'all':
    df = df[df['day_of_week'] == day.title()]


def day_w_1():
    df = pd.read_csv(CITY_DATA[city])
    df['Start Time'] = pd.to_datetime(df['Start Time'])
    df['week'] = df['Start Time'].dt.weekday_name
    day_w = df['week'].mode()
    print("\nThe most common day of the week in ",city,"was: ",day_w)


def hour_day_2():
    df = pd.read_csv(CITY_DATA[city])
    df['Start Time'] = pd.to_datetime(df['Start Time'])
    df['hour'] = df['Start Time'].dt.hour
    hour_m = df['hour'].mode()
    print("The most common hour of the day in ",city,"was: ",hour_m)


def month_3():
    df['month'] = df['Start Time'].dt.month
    month_m = df['month'].mode()


def start_st_4():
    new_frame = pd.read_csv(CITY_DATA[city])
    nf_count = new_frame['Start Station'].value_counts()
    text_1 = nf_count.head(1)
    print("\nThe most common Start Station in ",city," was: ",text_1)

def end_s_5():
    new_frame = pd.read_csv(CITY_DATA[city])
    nf_count2 = new_frame['End Station'].value_counts()
    text_2 = nf_count2.head(1)
    print("The most common End Station in ",city," was: ",text_2)

def duration_6():
    new_frame = pd.read_csv(CITY_DATA[city])
    nf_count3 = new_frame['Trip Duration'].sum()
    print("\nThe total duration of trips in ",city," was: ",nf_count3)

def average_7():
    new_frame = pd.read_csv(CITY_DATA[city])
    nf_count4 = new_frame['Trip Duration'].mean()
    print("\nThe average travel time in ",city," was: ",nf_count4)

def user_t_8():
    new_frame = pd.read_csv(CITY_DATA[city])
    user_types = new_frame['User Type'].value_counts()
    print ("\nThe count for each user types in ",city," was: ")
    print(user_types)

def finish_02():
    now_b = datetime.now()
    result_time = (now_b - now_a)
    print("\nThis program took only ",result_time," to run.")
    print("\nEnd of Work.")
    quit()

def user_g_9():
    new_frame_2 = pd.read_csv(CITY_DATA[city])
    user_gender = new_frame_2['Gender'].value_counts()
    print("The count for each gender of the users in ",city," was: ")
    print(user_gender)
    time.sleep(2)


def further():
    df = pd.read_csv(CITY_DATA[city])
    view_data = input('\nWould you like to view 5 rows of individual trip data? Please, enter yes or no:\n')
    view_data = view_data.lower()
    start_loc = 0
    while (view_data == 'yes'):
        print(df.iloc[start_loc:start_loc+5])
        start_loc += 5
        view_data = input("Do you wish to continue? Please, enter yes or no: \n").lower()


def main():
    day_w_1()
    hour_day_2()
    month_3()
    start_st_4()
    end_s_5()
    duration_6()
    average_7()
    user_t_8()

    if city.lower() == "washington":
        print("\nGender data not available for Washington.\n\n")
        further()
        finish_02()

    if (city.lower()) == "new york city":
        user_g_9()
        further()
        finish_02()

    if (city.lower()) == "chicago":
        user_g_9()
        further()
        finish_02()

if __name__ == "__main__":
    try:
        main()
    except:
        finish_02()
