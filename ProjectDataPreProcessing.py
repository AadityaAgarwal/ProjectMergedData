import csv

data=[]

with open("bright_stars.csv",'r') as f:
    csvread=csv.reader(f)

    for row in csvread:
        data.append(row)

headers=data[0]
planetData=data[1:]

for dataPoint in planetData:
    dataPoint[0]=dataPoint[0].lower()

planetData.sort(key=lambda planetData:planetData[2])
