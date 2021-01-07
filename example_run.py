from make_csv import make_csv
from clean_igra import clean_igra

# input your station ID code into the station variable
station = 'USM00072493'     # Oakland is the example

# input your text file that you downloaded from IGRA into the text_file variable
text_file = 'USM00072493-data.txt'    # this year to date OAK data is included in the repository as an example

# input the earliest year for which you want data
start = 2020
# input the last year of data you want + 1, 
stop = 2021     # I'm just using 2020 in the example so only 1 year of the 3 years of data created will be cleaned.

# Input a name you want for your cleaned files 
# or just set it to the station variable if you want to use the station ID
name = 'OAK'

# make a csv for each year contained in the dataset
make_csv(text_file)

# Clean the desired range of csv files
clean_igra(start, stop, station, name)

# In this example my folder now has 3 csvs created from the text file:
# USM00072493_2018.csv
# USM00072493_2019.csv
# USM00072493_2020.csv
# and one clean OAK_2020.csv file 