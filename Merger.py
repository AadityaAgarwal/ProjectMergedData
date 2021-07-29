import csv

dataset1=[]
dataset2=[]

with open("bright_stars.csv",'r') as f:
    csvread=csv.reader(f)

    for row in csvread:
        dataset1.append(row)
 
with open("dwarf_stars.csv",'r') as f:
    csvread=csv.reader(f)

    for row in csvread:
        dataset2.append(row)

header1=dataset1[0]
planetData1=dataset1[1:]

header2=dataset2[0]
planetData2=dataset2[1:]

headers=header1+header2

planetData=[]

for index,datarow in enumerate(planetData1):
    planetData.append(planetData1[index]+planetData2[index])


with open("ProjectFinalMerged.csv",'a+') as f:
    csvwriter=csv.writer(f)
    csvwriter.writerow(headers)
    csvwriter.writerows(planetData)
