import csv

'''stats_rows=[]
with open('srg_daily_stats.csv', 'r') as file:
    reader = csv.reader(file)
    for row in reader:
        stats_rows.append(row)
print (len(stats_rows))
print (stats_rows)
if len(stats_rows)==12:
    print("d3 got")'''



# data to be written row-wise in csv fil
data = [['Geeks for Geeks', '2008', 'Sandeep Jain'],
        ['HackerRank', '2009', 'Vivek Ravisankar']]

# opening the csv file in 'a+' mode
file = open('g4g.csv', 'a+', newline ='')

# writing the data into the file
with file:
    write = csv.writer(file)
    write.writerows(data) 
