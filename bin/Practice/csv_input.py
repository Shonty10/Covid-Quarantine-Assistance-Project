import csv
fields=['name','eng','math','phy','comp','chem']
rows=[]
name=input("enter name:")
marks_e=float(input("enter marks for eng:"))
marks_m=float(input("enter marks for math:"))
marks_p=float(input("enter marks for phy:"))
marks_co=float(input("enter marks for comp:"))
marks_ch=float(input("enter marks for chem:"))
totmarks=marks_e+marks_m+marks_p+marks_co+marks_ch
avgmarks=totmarks/5
rows.append([name,marks_e,marks_m,marks_p,marks_co,marks_ch,totmarks,avgmarks])
print(rows)
    
with open("studentmarks.csv","a") as csvfile:
    csvwriter=csv.writer(csvfile)
    csvwriter.writerow(fields)
    csvwriter.writerows(rows)
