#!/usr/bin/env python
# coding: utf-8

# In[1]:


import time
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
CITY_DATA = { 'chicago': 'chicago.csv',
              'new york': 'new_york_city.csv',
              'washington': 'washington.csv' }


# In[2]:


def get_filters():
    """
    Asks user to specify a city, month, and day to analyze.

    Returns:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    """
    print('Hello! Let\'s explore some US bikeshare data!')
    # TO DO: get user input for city (chicago, new york city, washington). HINT: Use a while loop to handle invalid inputs
    while True:
        city = input("Would you like to see data for Chicago, New York, or Washington? ").lower()
        if city in ['chicago', 'new york', 'washington']:
            break
        else:
            print("INVALID, please restart the program and choose true value")

    # TO DO: get user input for month (all, january, february, ... , june)
    #input = input("Would you like to filter the data by month, day, or not at all? Please if not write None")
    while True:
        month = input("Which month - January, February, March, April, May, June or all? ").lower()
        if month in ['january', 'february', 'march', 'april', 'may', 'june', 'all']:
            # use the index of the months list to get the corresponding int
            months = ['january', 'february', 'march', 'april', 'may', 'june', 'all']
            break
        else:
            print("this is an invalid input")

    
    # TO DO: get user input for day of week (all, monday, tuesday, ... sunday)
    while True:
        day = input("Which day - Monday, Tuesday, Wednesday, Thursday, Friday, Saturday, or Sunday? if all just type 'all' ").lower()
        if day in ['sunday', 'monday', 'tuesday', 'wednesday', 'thursday', 'friday', 'saturday', 'all']:
            break
            # use the index of the months list to get the corresponding int
#             days = {"Monday":2, "Tuesday":3, "Wednesday":4, "Thursday":5, "Friday":6, "Saturday":7, "Sunday":1}
#             day = days.index(day) + 1
#         elif day == 'all':
#             day = days.index() + 1
        else:
            print("this is invalid input")



    print('-'*40)
    return city, month, day


# In[3]:


def load_data(city, month, day):
    """
    Loads data for the specified city and filters by month and day if applicable.

    Args:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    Returns:
        df - Pandas DataFrame containing city data filtered by month and day
    """
    # load data file into a dataframe
    df = pd.read_csv(CITY_DATA[city], index_col= False)
    # convert the Start Time column to datetime
    df['Start Time'] = pd.to_datetime(df['Start Time'])
    # extract month and day of week from Start Time to create new columns
    df['month'] = df['Start Time'].dt.month
#     df['day_of_week'] = df['Start Time'].dt.weekday_name
    df['day_of_week'] = df['Start Time'].dt.day_name()
    # extract hour from the Start Time column to create an hour column
    df['hour'] = df['Start Time'].dt.hour
    # filter by month if applicable
    if month != 'all':
        # use the index of the months list to get the corresponding int
        months = ['january', 'february', 'march', 'april', 'may', 'june']
        month = months.index(month) + 1    
        # filter by month to create the new dataframe
        df = df[df['month'] == month]

    # filter by day of week if applicable
    if day != 'all':
        # filter by day of week to create the new dataframe
        df = df[df['day_of_week'] == day.title()]



    return df


# In[4]:


def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()

    # TO DO: display the most common month

    popular_month = df['month'].mode()[0]
    print('Most Common Month:', popular_month)
#     df['month'].plot(kind='scatter',x='Users',y='month',color='red')
#     plt.show()

    # TO DO: display the most common day of week
    popular_day_of_week = df['day_of_week'].mode()[0]
    print('Most Common day of the week:', popular_day_of_week)

    # TO DO: display the most common start hour
    popular_hour = df['hour'].mode()[0]
    print('Most Frequent Start Hour:', popular_hour)


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


# In[5]:


def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # TO DO: display most commonly used start station
    popular_station = df['Start Station'].mode()[0]
    print("Most commonly used start station is : ", popular_station)
#     plt.figure()
#     x1 = df['Start Station']
#     y1 = popular_station
#     plt.plot(x1,y1)

    


    # TO DO: display most commonly used end station
    popular_end_station = df['End Station'].mode()[0]
    print("Most commonly used end station is : ", popular_end_station)
#     plt.figure()
#     x2 = df['End Station']
#     y2 = popular_end_station
#     plt.plot(x2,y2)




    # TO DO: display most frequent combination of start station and end station trip
    df['frequent_combination'] = df['Start Station'] + " " + df['End Station']
    print("The most frequent combination of start station and end station trip is: ", df['frequent_combination'].mode()[0])
#     plt.figure()
#     x3 = df['frequent_combination']
#     y3 = df['Start Station']
#     y03 = df['End Station']
#     plt.plot(x3,y3)
#     plt.plot(x3,y03)



    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


# In[6]:


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # TO DO: display total travel time
    total_time = df['Trip Duration'].sum()
    print("Total time travelled is: ", total_time)


    # TO DO: display mean travel time
    mean_time = df['Trip Duration'].mean()
    print("Mean time travelled is: ", mean_time)


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


# In[7]:


def user_stats(df, city):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # TO DO: Display counts of user types
    user_types = df['User Type'].value_counts()
    print(user_types)

    if city != 'washington': ## since washington doesn't have gender nor Birth year columns so we had to puth that condition
        ## and we added an additional attribute in user_stats refers to city
    # TO DO: Display counts of gender
        g = df['Gender'].value_counts()
        print(g)


    # TO DO: Display earliest, most recent, and most common year of birth
        birh_min = df['Birth Year'].min()
        print("most recent DOB is: ",birth_min)

        birh_max = df['Birth Year'].max()
        print("most earliest DOB is: ",birth_max)

        birth_com = df['Birth Year'].mode()
        print("most common DOB is: ",birth_com)


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


# In[8]:


def display_raw_data(df):
    """
    Asks if the user would like to see some lines of data from the filtered dataset.
    Displays 5 (show_rows) lines, then asks if they would like to see 5 more.
    Continues asking until they say stop.
    """
    show_rows = 5
    rows_start = 0
    rows_end = show_rows - 1    # use index values for rows

    print('Would you like to see the dataframe of the current dataset?')
    while True:
        raw_data = input("yes or no: ")
        if raw_data.lower() == 'yes':
            # display show_rows number of lines, but display to user as starting from row as 1
            # e.g. if rows_start = 0 and rows_end = 4, display to user as "rows 1 to 5"
            print('Displaying rows {} to {}:'.format(rows_start + 1, rows_end + 1))

            print(df.iloc[rows_start : rows_end + 1])
            rows_start += show_rows
            rows_end += show_rows

            print('Would you like to see the next {} rows?'.format(show_rows))
            continue
        else:
            break


# In[13]:


def main():
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)

        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df, city)
        display_raw_data(df)
        
        print('Thanks that\'s all what I\'ve for you if you want to restart just re-run the program')

        restart = input('Would you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break



# In[14]:


if __name__ == "__main__":
    main()


# In[ ]:





# In[ ]:





# In[ ]:




