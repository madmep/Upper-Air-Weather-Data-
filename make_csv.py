import pandas as pd
def make_csv(filename): 
    '''(str)-> 'str'
    Input a file name for a NOAA IGRA data text file.  
    Returns 'Complete' when done.
    Creates a csv for each year of data that is in the input file.
    Does not clean or modify the data.
    '''
    # Open the file
    with open(filename) as f:
        # read in first line of data
        header = f.readline()   
        # if there's still data in the file keep reading it in
        while header:   
            # create a new file for each year of the data
            year = header[13:17]
            title = header[1:12] + '_' + year + '.csv'
            # create a list for each column 
            yr = []
            month = []
            day = []
            hour = []
            reltime = []
            p_src = []
            np_src = []
            lat = []
            long = []
            lvl_1 = []
            lvl_2 = []
            e_time = []
            pressure = []
            pflag = []
            gph = [] 
            zflag = []
            temp = [] 
            tflag = []
            rh = [] 
            dew_drop = [] 
            wdir = []
            wspd = []

            ''' 
            Each year gets it's own csv created, if it's the same year, we keep adding to the lists.
            If the year has changed it will kick you out to save the current lists as a csv
            then re enter the while loop above starting a new file for the new year.
            '''
            while year == header[13:17]:
                # each header row has data that's repeated for every sounding observation
                # save it once here and then just keep adding it for each row in the inner loop below
                n = int(header[32:36])   # number of observations under each header's information
                y = header[13:17]
                m = header[18:20]
                d = header[21:23]
                h = header[24:26]
                r = header[27:31]
                p = header[36:45]
                np = header[45:54]
                la = header[56:63]
                lo = header[63:71]

                # for each row of sounding data under the header information (there are n rows)
                for i in range(n):
                    # read in a row of data
                    row = f.readline()
                    # add a value for each row from the header constants for each observation that we created above
                    yr.append(y)
                    month.append(m)
                    day.append(d)
                    hour.append(h)
                    reltime.append(r)
                    p_src.append(p)
                    np_src.append(np)
                    lat.append(la)
                    long.append(lo)
                    # add this row's data to each column's list
                    lvl_1.append(row[0])
                    lvl_2.append(row[1])
                    e_time.append(row[3:8])
                    pressure.append(row[9:15])
                    pflag.append(row[15])
                    gph.append(row[16:21])
                    zflag.append(row[21])
                    temp.append(row[22:27])
                    tflag.append(row[27])
                    rh.append(row[28:33])
                    dew_drop.append(row[34:39])
                    wdir.append(row[40:45])
                    wspd.append(row[46:51])
                
                # read in the next header row to check if it's the same year at the top of the while loop
                header = f.readline()

            # once a year is complete we make a dictionary 
            data = {'year': yr, 'month': month, 'day': day, 'hour':hour, 'rel_time':reltime, 'p_src': p_src,\
                    'np_src':np_src, 'lat': lat, 'long': long, 'lvl_1': lvl_1, 'lvl_2': lvl_2, \
                    'e_time':e_time, 'pressure': pressure, 'pflag': pflag,'gph':gph,\
                    'zflag':zflag, 'temp':temp, 'tflag':tflag, 'rh':rh, 'dew_drop':dew_drop, \
                    'wdir':wdir, 'wspd':wspd}
            # turn the dictionary into a dataframe
            df = pd.DataFrame(data)
            # save the dataframe as a csv and use the station ID and year for its name
            df.to_csv(title, index=False)
            # will loop again to see if there's another header row of data
    
    # When there is no more data to be read in from the text file       
    return "Complete"