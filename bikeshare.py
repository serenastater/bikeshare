import time
import pandas as pd
import numpy as np

CITY_DATA = { 'chicago': 'chicago.csv',
              'new york city': 'new_york_city.csv',
              'washington': 'washington.csv' }

def get_filters():
    """
    Asks user to specify a city, month, and day to analyze.

    Returns:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month
                      filter
        (str) day - name of the day of week to filter by, or "all" to apply no
                    day filter
    """
    print('Hello! Let\'s explore some US bikeshare data!')
    # TO DO: get user input for city (chicago, new york city, washington).
    # HINT: Use a while loop to handle invalid inputs
    while True:
        try:
            city = str(input("You may see stats from either Chicago, New York \
            City, or Washington. Please enter your chosen city! ").lower())
        except:
            print("Sorry, I didn't understand that.")
            continue

        if city.lower() not in ('chicago', 'new york city', 'washington'):
            print("Sorry, I didn't understand that.")
        else:
            break
        # TO DO: get user input for month (all, january, february, ... , june)
    while True:
        try:
            month = str(input("For which month would you like to see {}'s data? \
            If you would like to see an entire calendar year, please specify \
            'all'. ".format(city.title())))
        except:
            print("Sorry, I didn't understand that.")
            continue

        if month.lower() not in ('january', 'february', 'march', 'april', 'may',
        'june', 'july', 'august', 'september', 'october', 'november', 'december'):
            print("Sorry, I didn't understand that.")
        else:
            break
        # TO DO: get user input for day of week (all, monday, tuesday, ... sunday)
    while True:
        try:
            day = int(input("For which day of {} would you like to see data? \
            If you would like to see the entire month, please specify \
            'all'. ".format(month.title())))
        except:
            print("Sorry, I didn't understand that.")
            continue

        if day not in range(31):
            print("Sorry, I didn't understand that.")
        else:
            break

    print('-'*50)
    return city, month, day

get_filters()
#
# def load_data(city, month, day):
#     """
#     Loads data for the specified city and filters by month and day if applicable.
#
#     Args:
#         (str) city - name of the city to analyze
#         (str) month - name of the month to filter by, or "all" to apply no month filter
#         (str) day - name of the day of week to filter by, or "all" to apply no day filter
#     Returns:
#         df - Pandas DataFrame containing city data filtered by month and day
#     """
#
#
#     return df
#
#
# def time_stats(df):
#     """Displays statistics on the most frequent times of travel."""
#
#     print('\nCalculating The Most Frequent Times of Travel...\n')
#     start_time = time.time()
#
#     # TO DO: display the most common month
#
#
#     # TO DO: display the most common day of week
#
#
#     # TO DO: display the most common start hour
#
#
#     print("\nThis took %s seconds." % (time.time() - start_time))
#     print('-'*40)
#
#
# def station_stats(df):
#     """Displays statistics on the most popular stations and trip."""
#
#     print('\nCalculating The Most Popular Stations and Trip...\n')
#     start_time = time.time()
#
#     # TO DO: display most commonly used start station
#
#
#     # TO DO: display most commonly used end station
#
#
#     # TO DO: display most frequent combination of start station and end station trip
#
#
#     print("\nThis took %s seconds." % (time.time() - start_time))
#     print('-'*40)
#
#
# def trip_duration_stats(df):
#     """Displays statistics on the total and average trip duration."""
#
#     print('\nCalculating Trip Duration...\n')
#     start_time = time.time()
#
#     # TO DO: display total travel time
#
#
#     # TO DO: display mean travel time
#
#
#     print("\nThis took %s seconds." % (time.time() - start_time))
#     print('-'*40)
#
#
# def user_stats(df):
#     """Displays statistics on bikeshare users."""
#
#     print('\nCalculating User Stats...\n')
#     start_time = time.time()
#
#     # TO DO: Display counts of user types
#
#
#     # TO DO: Display counts of gender
#
#
#     # TO DO: Display earliest, most recent, and most common year of birth
#
#
#     print("\nThis took %s seconds." % (time.time() - start_time))
#     print('-'*40)
#
#
# def main():
#     while True:
#         city, month, day = get_filters()
#         df = load_data(city, month, day)
#
#         time_stats(df)
#         station_stats(df)
#         trip_duration_stats(df)
#         user_stats(df)
#
#         restart = input('\nWould you like to restart? Enter yes or no.\n')
#         if restart.lower() != 'yes':
#             break
#
#
# if __name__ == "__main__":
# 	main()
