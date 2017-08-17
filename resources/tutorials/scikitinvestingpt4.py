# https://www.youtube.com/watch?v=rAdAVcS4aL0
# parsing data 

# to download the data: 
# pythonprogramming.net/downloads/intraQuarter.zip <-- downloads

# analyzing debt to equity ratio 

# 12 is to 1 as 13.75 is to x, for conversion, and we would solve for x, algorithm for determining to range

# machine learning shines the brightest when you can compare 50+ features

# if on windows go to www.lfd.uci.edu for libraries

import pandas as pd
import os
import time
from datetime import datetime

# file name is the date

path = "X:/Backups/intraQuarter" # path is likely different


def Key_Stats(gather="Total Debt/Equity (mrq)"):
    statspath = path+'/_KeyStats'
    # trying to get list of stocks
    stock_list = [x[0] for x in os.walk(statspath)] # going to gather all the names for the directory contents
    # print(stock_list)

    for each_dir in stock_list[1:]:
        each_file = os.list(each_dir) # lists out all the directories for the first directory, all the file names
        ticker = each_dir.split("//")[1]
        print(each_file)
        if len(each_file) > 0: # if we have something, perhaps no data
            for file in each_file:
                # now we're ready to begin to pull data
                date_stamp = datetime.strptime(file, '%Y%m%d%H%M%S.html') # strip time from file
                unix_time = time.mktime(date_stamp.timetuple())
                print(date_stamp, unix_time)
                time.sleep(15)
                # now we have stock name and time stamp for the data that we're about to collect 
                # we want to get to the total debt to equity ratio
                
                # to open up a file
                full_file_path = each_dir+'/'+file
                print(full_file_path)
                source = open(full_file_path, 'r').read() # get source code 
                print(source)
                
                # now pull value that we want
                value = source.split(gather+':</td><td class = "yfnc_tabledata1">')[1].split('</td>')[0]
                 # use element 1 since comes before is on the left size, 0 on the right size 
                
                # let's print the ticker now and the debt to equity ratio
                print(ticker+":", value) # gives ticker and debt to equity ratio
                # so we parsed the data, we aquired the data
                
                # let's now save the data so we can access later
                # end of tutorial 
                                                                                            
                
                
                
# parsing, find number, and element right before number, veiew source, control f, 
                
                
                
                
                
    
    
    
    
  
Key_Stats() # big list of all the directories 



  




