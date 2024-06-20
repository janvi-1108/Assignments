
import csv
with open(r"C:\Users\DELL\Desktop\Coding\Python\Emp.CSV", 'r') as file:
    rdr=csv.reader(file)
    for row in rdr:
        print(row)