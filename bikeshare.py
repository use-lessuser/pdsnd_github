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
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    """
    print('Hello! Let\'s explore some US bikeshare data!')
    # TO DO: get user input for city (chicago, new york city, washington). HINT: Use a while loop to handle invalid inputs
    city = ''
    while city not in ('chicago', 'new york', 'washington'):
        city = str(input('Would you like to see the data for Chicago, New York, or Washington?')).lower()
        if city not in ('chicago', 'new york', 'washington'):
            print('That\'s not a valid input')    
 
    # TO DO: get user input for month (all, january, february, ... , june)
    month = ''
    while month not in ['january', 'february', 'march', 'april', 'may', 'june', 'all']:
        month = str(input('Which month? january, february, march, april, may, or june?')).lower()
        if month not in ['january', 'february', 'march', 'april', 'may', 'june', 'all']:
            print('That\'s not a valid input')   


    # TO DO: get user input for day of week (all, monday, tuesday, ... sunday)
    day = ''
    while day not in ['monday', 'tuesday', 'wednesday', 'thursday', 'friday', 'saturday', 'sunday', 'all']:
        day = str(input('Which day? Monday, Tuesday, Wednesday, Thursday, Friday, Saturday, or Sunday')).lower()
        if day not in ['monday', 'tuesday', 'wednesday', 'thursday', 'friday', 'saturday', 'sunday', 'all']:
            print('That\'s not a valid input')


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
    
    # load data file into a dataframe
    df = pd.read_csv(CITY_DATA[city])
    
    # convert the Start Time column to datetime
    df['Start Time'] = pd.to_datetime(df['Start Time'])
    # extract month and day of week from Start Time to create new columns
    df['month'] = df['Start Time'].dt.month
    df['day_of_week'] = df['Start Time'].dt.weekday_name

    # filter by month if applicable
    if month != 'all':
        # use the index of the months list to get the corresponding int
        months = ['january', 'february', 'march', 'april', 'may', 'june']
        month = months.index(month) +1
        # filter by month to create the new dataframe
        df = df[df['month'] == month]
    # filter by day of week if applicable
    if day != 'all':
        
        # filter by day of week to create the new dataframe
        df = df[df['day_of_week'] == day.title()]

    return df


def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()
    
    df['hour'] = df['Start Time'].dt.hour
    
    # TO DO: display the most common month
    popular_month = df['month'].mode()[0]
    print('The most frequent month:', popular_month)
    # TO DO: display the most common day of week
    popular_day = df['day_of_week'].mode()[0]
    print('The most frequent day of the week:', popular_day)
    # TO DO: display the most common start hour
    popular_start_hour = df['hour'].mode()[0]
    print('The most frequent hour of the day:', popular_start_hour)

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()
    
    df['Stations'] = df['Start Station'] + (' - ') + df['End Station']
    #print(df['Stations'])
    # TO DO: display most commonly used start station
    popular_start_station = df['Start Station'].value_counts().idxmax()
    print('The most popular start station:', popular_start_station)
    # TO DO: display most commonly used end station
    popular_end_station = df['End Station'].value_counts().idxmax()
    print('The most popular end station:', popular_end_station)
    # TO DO: display most frequent combination of start station and end station trip
    popular_combi_station = df['Stations'].value_counts().idxmax()
    print('The most popular combination of start station and end station:', popular_combi_station)

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # TO DO: display total travel time, for this you have to subtract the starting Timestamp (1970-01-10)
    total_travel_time = df['Trip Duration'].sum()
    total_travel_time = pd.to_datetime(total_travel_time, unit = 's') - pd.Timestamp("1970-01-01")
    print('The total travel time is:', total_travel_time)
    # TO DO: display mean travel time, for this you have to subtract the starting Timestamp (1970-01-10)
    average_travel_time = df['Trip Duration'].mean()
    average_travel_time = pd.to_datetime(average_travel_time, unit = 's') - pd.Timestamp("1970-01-01")
    print('The average travel time is:', average_travel_time)

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def user_stats(df):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # TO DO: Display counts of user types
    number_user_types = df['User Type'].value_counts()
    print('The number of users by user type:', number_user_types)
    # TO DO: Display counts of gender
    if ('Gender') in df:
        number_user_gender = df['Gender'].value_counts()
        print('The number of users by gender:', number_user_gender)
    else:
        print('Information about gender is not available for this city')
    # TO DO: Display earliest, most recent, and most common year of birth
    if ('Birth Year') in df:
        oldest = df['Birth Year'].min()
        print('The earliest year of birth among users:', oldest)
        youngest = df['Birth Year'].max()
        print('The most recent year of birth among users:', youngest)
        common = df['Birth Year'].mode()
        print('The most common year of birth among users:', common)
    else:
        print('Information about birth year is not available for this city')

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)

def raw_data(df):
    i = 0
    while True:
        raw_data = str(input('Do you want to see raw data? yes / no'))
        if raw_data.lower() != 'yes':
            break
        else:
            print(df.iloc[i:i+5])
            i += 5
            
def main():
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)

        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df)
        raw_data(df)
                       
        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break


if __name__ == "__main__":
	main()

    
# sources: google search, results mostly from stack overflow 