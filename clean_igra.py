import pandas as pd 
import numpy as np

# If you want a cardinal direction column in your final dataset
def cardinal_wind(dir):
    '''
    Applied to a series of directions in degrees from north
    Returns a series with compass rose categorical values 
    '''
    if dir > 338 or dir <= 23:
        return 'N'
    elif dir > 23 and dir <= 68:
        return 'NE'
    elif dir > 68 and dir <= 113:
        return 'E'
    elif dir > 113 and dir <= 158:
        return 'SE'
    elif dir > 158 and dir <= 203:
        return 'S'
    elif dir > 203 and dir <= 248:
        return 'SW'
    elif dir > 248 and dir <= 293:
        return 'W'
    else:
        return 'NW'

def clean_igra(start, stop, station, name):
    '''(str) -> str
    Input the earliest year of the csvs you want to work with, the last year of data you want, 
    the station ID from the filenames, and the name you want to use for the clean files.
    
    Creates a csv with no blank values, and with standardised null values as np.NaN.
    Returns 'Complete' when done.
    
    Converts some units from tenths or hundreths so it's easier to understand the data.
    Adds a column for cardinal wind direction.
    Adds a column for pressure altitude in feet.
    Allows the option to convert speed to knots and height from meters to feet.
    
    clean_igra(1944, 2021, 'USM00072493', 'OAK')
        creates a cleaned csv labeled 'OAK_year.csv' for each year of data between 1944 and 2020.
    > 'Complete'
    '''
    # create a file for each year in the input range
    for year in range(start, stop):
        df = pd.read_csv(station + '_' + str(year) + '.csv')
        
        # get rid of 'blank' as a flag value for the three flag columns
        for col in ['pflag', 'zflag', 'tflag']:
            df[col] = df[col].apply(lambda x: 'C' if x == ' ' else x)
        
        # Turn -8888 and -9999 into NaN
        cols = ['pressure', 'gph', 'temp', 'rh', 'dew_drop', 'wdir', 'wspd', 'rel_time', 'e_time']
        for col in cols:
            df[col] = df[col].apply(lambda x: np.nan if (x == -9999 or x == -8888) else x)

        # Create a cardinal direction column
        df['cardinal'] = df.wdir.apply(cardinal_wind)
        
        # Pressure column in mb
        df.pressure = df.pressure.apply(lambda x: x/100)
        
        # Create a pressure altitude column
        df = df[~df['pressure'].isnull()]
        df['press_alt_ft'] = df.pressure.apply(lambda x: round(145366.45 * (1 - (x/1013.25)**.190284)))

        # Turn temp and percent humidity from tenths into full degrees C or %
        df.temp = df.temp.apply(lambda x: x/10)
        df.rh = df.rh.apply(lambda x: x/10)
        df.dew_drop = df.dew_drop.apply(lambda x: x/10)
        
        '''
        Uncomment lines of code provided below if you want your windspeed
        units to be knots, or your gph in feet.
        Beware you will introduce rounding error.
        '''
        # df.wspd = df.wspd.apply(lambda x: round((x/10) * 1.943844,2))
        # df.gph = df.gph.apply(lambda x: round(x/3.28084, 2)
        
        df.to_csv(name + '_' + str(year) + '.csv')
    
    # When done with all the csvs in the date range 
    return 'Complete'