import os.path
from os import path
import csv


t1='yolo'

filename = t1+"_"+"daily_stats.csv"
rand=[]
rand.append(t1)
rand.append(filename)

def day_no_check():

    global day_count
    if path.exists(filename)==False:
        day_count='Welcome to day 1'
    else:
        global pre_stats_rows
        pre_stats_rows=[]
        with open(filename, 'r') as file:
            reader = csv.reader(file)
            for row in reader:
                pre_stats_rows.append(row)
        if len(pre_stats_rows)==4:
            day_count='Welcome to day 2'
        elif len(pre_stats_rows)==8:
            day_count='Welcome to day 3'
        elif len(pre_stats_rows)==12:
            day_count='Welcome to day 4'
        elif len(pre_stats_rows)==16:
            day_count='Welcome to day 5'
        else:
            day_count= 'Day Count Limit Reached'

day_no_check()
print(day_count)
