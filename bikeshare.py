import time
import pandas as pd
import numpy as np
#Added additional comment for git project!
CITY_DATA = { 'chicago': 'chicago.csv',
              'new york city': 'new_york_city.csv',
              'washington': 'washington.csv' }  
months = ['all', 'january', 'february', 'march', 'april', 'may', 'june']
days = ['all', 'sunday', 'monday', 'tuesday', 'wednesday', 'thursday', 'friday', 'saturday']
answers = ['yes', 'no']
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
    city = ''
    while city.lower() not in CITY_DATA:
        city = input("Please enter a city you would like to see data for: chicago, new york city, or washington:").lower()
        if city.lower() in CITY_DATA:
            #We were able to get the name of the city to analyze data.
            city = CITY_DATA[city.lower()]
            break
        else:
            #city input wasn't listed in CITY_DATA list.
            print("You entered " + str(city) + " which isn't an option.")
    
    # TO DO: get user input for month (all, january, february, ... , june)
    month_input = ''
    while month_input.lower() not in months:
        month_input = input("Would you like to filter the data by month, or not at all? Please enter one of the following month options: january, february, march, april, may, june, or all:")
        if month_input.lower() in months:
            #month_input IS listed in months list above.
            month = month_input.lower()
        else:
            #month_input IS NOT listed in months list above.
            print("You entered " + month_input + " which isn't a listed city. Please enter one of the following month options: january, february, march, april, may, june, or all:")
 
    # TO DO: get user input for day of week (all, monday, tuesday, ... sunday)
    day_input = ''
    while day_input.lower() not in days:
        day_input = input("Would you like to filter the data by day or not at all? - monday, tuesday, wednesday, thursday, friday, saturday, sunday, or all:")
        if day_input.lower() in days:
             #day_input IS listed in days list above.
            day = day_input.lower()
        else:
            #day_input IS NOT listed in days list above.
            print("You entered " + day_input +" which isn't an option. Please enter one of the following month options: monday, tuesday, wednesday, thursday, friday, saturday, sunday, or all:")    


    print('-'*40)
    return city, month, day


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
    df = pd.read_csv(city)
    # reads data and puts it in dataframe
    
    #convert time from Start Time column
    df['Start Time'] = pd.to_datetime(df['Start Time'])
    df['month'] = df['Start Time'].dt.month
    df['day_of_week'] = df['Start Time'].dt.weekday_name
    df['hour'] = df['Start Time'].dt.hour

    #filter by month
    if month != "all":
        #indexed months here
        month = months.index(month)

    return df


def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()

    # TO DO: display the most common month
    common_month = df['month'].mode()[0]
    print("The most popular month is: " + months[common_month].title())
    # TO DO: display the most common day of week
    common_day_of_week = df['day_of_week'].mode()[0]
    print("The most popular day of the week is: " + common_day_of_week)
    # TO DO: display the most common start hour
    common_start_hour = df['hour'].mode()[0]
    print("The most popular start hour is: " + str(common_start_hour))

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # TO DO: display most commonly used start station
    common_start_station = df['Start Station'].mode()[0]
    print("The most popular used start station location is: " + common_start_station)
    # TO DO: display most commonly used end station
    common_end_station = df['End Station'].mode()[0]
    print("The most popular used end station location is: " + common_end_station)
    # TO DO: display most frequent combination of start station and end station trip
    freq_start_end = (df['Start Station'] + "||" + df['End Station']).mode()[0]
    print('The most frequent combination of start station and end station is: ' + str(freq_start_end.split('||')))
    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # TO DO: display total travel time
    total_travel = df['Trip Duration'].sum()
    print("The total travel time is: " + str(total_travel))
    # TO DO: display mean travel time
    mean_travel = df['Trip Duration'].mean()
    print("The average travel time is: " + str(mean_travel))

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def user_stats(df, city):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # TO DO: Display counts of user types
    users_types = df['User Type'].value_counts()
    print("The user types listed is: \n" + str(users_types))

    # TO DO: Display counts of gender
    if  city == 'chicago.csv' or city == 'new_york_city.csv':
        gender_counts = df['Gender'].value_counts()
        print("The gender count is:\n" + str(gender_counts))
    
    # TO DO: Display earliest, most recent, and most common year of birth
        earliest_birth = df['Birth Year'].min()
        recent_birth = df['Birth Year'].max()
        common_birth = df['Birth Year'].mode()[0]
        print('The earliest birth year listed is: ' + str(int(earliest_birth)))
        print('The recent birth year listed is: ' + str(int(recent_birth)))
        print('The most common birth year listed is: ' + str(int(common_birth)))
    else: city == 'washington.csv'
    print('Washington does not capture gender or birth year data.')

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)
# TO DO: Ask user if they would like to see individual trip data? Enter yes or no
    view_index = 0
    print(df.head())
    view_data = ''
    while view_data != 'no': 
#when view_data input is entered incorrectly or no is entered it moves on to the next question: Would you like to restart?.         
        view_data = input("Would you like to view 5 more rows of individual trip data? Enter yes or no?").lower()
        if view_data.lower() != 'yes':
            break
        view_index = view_index + 5
        print(df.iloc[view_index:view_index +5])

def main():
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)

        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df, city)

        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break

if __name__ == "__main__":
    main()
