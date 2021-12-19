import time 
import calendar
import numpy as np
import pandas as pd
from termcolor import colored
from art import *

CITY_DATA = { 'chicago': 'chicago.csv',
              'new york city': 'new_york_city.csv',
              'washington': 'washington.csv' }

# test in my pc 
'''CITY_DATA = { 'chicago': 'D:\coursers\EGYFWD\professional\Bikeshare\chicago.csv',
              'new york city': 'D:\coursers\EGYFWD\professional\Bikeshare\new_york_city.csv',
              'washington': 'D:\coursers\EGYFWD\professional\Bikeshare\washington.csv' }'''
              

# First Function Done 
tprint('Thank You') 
aprint("butterfly")
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
    Art = text2art('FWD', font='block', chr_ignore=True)
    print(colored(Art,'green'))
    while True:
        city = input('select one city of (chicago, new york city, washington)\n').lower()
        if city in CITY_DATA.keys():
            break
        else :
            print('Please re enter a valid City !!')
            
            
    # TO DO: get user input for month (all, january, february, ... , june)
    Months = [calendar.month_name[i].lower() for i in range(0,7)]
    del(Months[0])
    Months.append('all')
    print(Months)
    while True:
        month = input('select which month (all, january, february, ... , june)\n').lower()
        if month in Months:
            break
        else :
            print('Please re enter a valid Month !!')
            

    # TO DO: get user input for day of week (all, monday, tuesday, ... sunday)
    Days = [calendar.day_name[i].lower() for i in range(0,7)]
    Days.append('all')
    print(Days)
    while True:
        day = input('select which day of week (all, monday, tuesday, ... sunday)\n').lower()
        if day in Days:
            break
        else :
            print('Please re enter a valid day !!')

    print('-'*40)
    return city, month, day

# Second Function Done 
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
    # AS Solved in Udacity Practice # Noteeeeee !! 
    ## I re uesd the Code .. ok !! 
    # load data file into a dataframe
    df = pd.read_csv(CITY_DATA[city])

    # convert the Start Time column to datetime
    df['Start Time'] = pd.to_datetime(df['Start Time'])

    # extract month and day of week from Start Time to create new columns
    df['month'] = df['Start Time'].dt.month
    df['day_of_week'] = df['Start Time'].dt.day_name()

    # filter by month if applicable
    if month != 'all':
        # use the index of the months list to get the corresponding int
        months = ['january', 'february', 'march', 'april', 'may', 'june']
        month =  months.index(month)

        # filter by month to create the new dataframe
        df = df[df['month'] == month]

    # filter by day of week if applicable
    if day != 'all':
        # filter by day of week to create the new dataframe
        # day.title() to be as Data Set 
        df = df[df['day_of_week'] == day.title()]

    return df
    
# Third Function Done 
def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()

    # TO DO: display the most common month
    common_month = colored(df['month'].mode()[0],'green')
    print(f'the most common month is : {common_month}')

    # TO DO: display the most common day of week
    common_day = colored(df['day_of_week'].mode()[0],'red')
    print(f'the most common day of week is : {common_day}')

    # TO DO: display the most common start hour
    df['start_hour'] = df['Start Time'].dt.hour
    common_hour = colored(df['start_hour'].mode()[0],'cyan')
    print(f'the most common start hour is : {common_hour}')


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # TO DO: display most commonly used start station
    start = colored(df['Start Station'].mode()[0],'green')
    print(f'the most commonly used start station is : {start}')

    # TO DO: display most commonly used end station
    end = colored(df['End Station'].mode()[0],'red')
    print(f'the most commonly used end station is : {end}')

    # TO DO: display most frequent combination of start station and end station trip
    most_popular_trip = df.groupby(['Start Station', 'End Station']).size().idxmax()
    #df['trip'] = df['Start Station'] + " , " + df['End Station']
    trip = colored(most_popular_trip.mode()[0],'cyan')
    print(f'the most frequent combination of start station and end station trip is : {trip}')

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # TO DO: display total travel time
    total_time = colored((df['Trip Duration'].sum()).round(),'green')
    print(f'the total travel time is : {total_time}')

    # TO DO: display mean travel time
    mean_travel_time = colored((df['Trip Duration'].mean()).round(),'red')
    print(f'the mean travel time is : {mean_travel_time}')

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def user_stats(df,city):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # TO DO: Display counts of user types
    user_df = df['User Type']
    counts_users = colored(user_df.value_counts().to_frame(),'cyan')
    print(f'Display counts of user types : {counts_users}')

    # TO DO: Display counts of gender
    
    if city != 'washington':
        Gend_df = df['Gender']
        gender = colored(Gend_df.value_counts().to_frame(),'blue')
        print(f'Display counts of gender : {gender}')
        
        # TO DO: Display earliest, most recent, and most common year of birth
        earliest = colored((df['Birth Year'].min()),'green')
        print(f'Display earliest year of birth is : {earliest}')
        
        recent = colored((df['Birth Year'].max()),'blue')
        print(f'Display most recent year of birth is : {recent}')
        
        common_year = colored((df['Birth Year'].mode()[0]),'red')
        print(f'Display most common year of birth is : {common_year}')
        
    else:
        print(colored('There is No information about washington !! ','red'))    


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)
    
    index = 5
    while True:
        user_input = input('\nWould you want to see some of raw data ? Enter (yes or other.)\n')
        if user_input.lower() == 'yes':
            print(colored(df.head(index),'yellow'))
            index += 5
        else:
            break


def main():
    while True:
        city, month, day = get_filters()
        print(city,month,day)
        df = load_data(city, month, day)

        time_stats(df) 
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df,city)

        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            Art = text2art("Bye Bye", font='block', chr_ignore=False)
            print(colored(Art,'red'))
            break
        
            


if __name__ == "__main__":
	main()
