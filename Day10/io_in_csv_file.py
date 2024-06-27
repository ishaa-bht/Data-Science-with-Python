import csv
#writing in csv file
csv_content = [
    ["Name", "Age", "Address"],
    ["Isha", 20, "Biratnagar"],
    ["Harry", 20, "London"]
]
with open ("example.csv", "w", newline="") as file:
    csv_writer = csv.writer(file)
    csv_writer.writerows(csv_content)

#Reading a csv file
with open ("example.csv","r",newline="") as file:
    csv_reader = csv.reader(file)
    csv_content = list(csv_reader)
    
for row in csv_content:
    print(row)

