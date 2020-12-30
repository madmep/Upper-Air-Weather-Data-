#  Making the NOAA IGRA Data Analysis Friendly

Find the upper air weather information you need and convert it into a clean and useful csv file.  If you need upper air weather information, you will most likely find the data you need in the NOAA [Integrated Global Radiosonde Archive](https://www.ncdc.noaa.gov/data-access/weather-balloon/integrated-global-radiosonde-archive) data.  This data is formatted in a way that you may find difficult to work with.  This project will help you find what you need and turn it into easy to use csv files.  
  
## Setup

You will need Python, Pandas and Numpy for the reading and cleaning of the data.  Matplotlib and Seaborn are only needed if you want to make the charts.  


## Useage 

You can see my [notebook](??) or follow these directions in order to:
* Find the datasets you need from the station and data lists
* Download the data as txt files
* Create csvs for each year in those files.
* Clean the csvs for easier analysis  

### Which Station's data do you need?
Find the station you need from this [list](https://www1.ncdc.noaa.gov/pub/data/igra/igra2-station-list.txt).  I have provided the station list as a [csv](???) in this repository so you can load it as a dataframe and apply parameters to find exactly the stations you are interested in.    

Column information is [here](https://www1.ncdc.noaa.gov/pub/data/igra/igra2-list-format.txt).  

You must note the station ID to find the data you want in the next step.  

### Download the data you want
* If you want current year data, find your station's ID in [this](https://www1.ncdc.noaa.gov/pub/data/igra/data/data-y2d/) list.
* If you want soundings for the full period of record find its ID on [this](https://www1.ncdc.noaa.gov/pub/data/igra/data/data-por/) list.
* Download the zip file with your station's id code from the appropriate list above.
* Get the text file out of the zip file and put it in the folder you're working out of. 

### Convert the text file into csvs for each year contained in the dataset and clean up the files you want to use for analysis.
* In main_loop.py 
    * you need to put your station's ID code in for the `station` variable value.
    * Insert the name of the text file you downloaded as the value for `text_file`
    * Then change the first year of data that you want cleaned for `start` value.
    * the last year of data you want to work with is the `stop` variable value.
    * `name` is what you want your final files to be called.  I use airport identifers.
        * set `name` = `station` if you want to use the station ID
* Once you run `main_loop` with your variable values you will have a csv for each year contained in the original text file you downloaded.  You will also have a csv for each year in your desired range that is ready for analysis.

### Changes made to 'clean' csv:
* -9999 and -8888 are used in a number of columns to identify missing data, we turned these into NaN.
* For flag columns blank, ' ', means the data has not been checked by tier 1 or 2 checks, but if the data is not missing it has passed all other checks.  We changed this into category 'C'.
* We've also created new categorical columns for cardinal wind direction and pressure altitude in feet.  
* We have the code to turn GPH into feet and wind speed into knots in the `clean_igra` function commented out.  It introduces rounding error so you may prefer to do conversions later in your analysis.  
* Values that were given in tenths or hundredths of degrees/percent/whatever have been changed to full values.
    * ex: 1 tenth of a degree C is now 0.1 degree C


## New Column Descriptions:

Original descriptions are [here](https://www1.ncdc.noaa.gov/pub/data/igra/data/igra2-data-format.txt)  
In that description you can find what the abbreviations mean and the units used.
|Column    |Description|
|:---------|-----------|
| month   |The month 1-12 of the sounding
| day     |Day of the month of the sounding
| hour    |Hour of the sounding in UTC
| rel_time|Release time of sounding UTC HHMM
| p_src   |Source of the pressure levels in the sounding.
| np_src  |Source of the non-pressure levels in the sounding
| lat     |Latitude of sounding
| long    |Longitude of sounding
| lvl_1   |Major level type indicator (1,2,3)
| lvl_2   |Minor level type indicator (1,2,0)
| e_time  |Elapsed time since launch MMSS
| pressure|Reported pressure in mb 
| pflag   |Pressure flag (A,B,C)
| gph     |Geopotential height in meters if you didn't uncomment the conversion code
|    | geopotential height in ft above sea level if you used the conversion code
| zflag   |GPH processing flag (A,B,C)
| temp    |Temperature in degrees Celsius
| tflag   |Temp processing flag (A,B,C)
| rh      |Relative humidity in percent
| dew_drop|Dewpoint depression in degrees C
| wdir    |Wind direction in degrees from north (0-359)
| wspd    |Wind speed in tenths of meters per second if you didn't uncomment the conversion code
|    |wind speed in knots if you did uncomment conversion code
| cardinal|Wind direction in cardinal direction 
| p_alt_ft|Pressure altitude in feet
