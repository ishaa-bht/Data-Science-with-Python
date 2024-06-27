import json 

with open("students.json","r") as file:
    json_content= json.load(file)
    # print(json_content)
new_student_record=[]
from functools import reduce
def add_two_numbers(num1,num2):
        return num1 + num2


for record in json_content:
    marks = 0
    print("================================================================================")
    marks= record["marks"]
    total_marks = reduce(add_two_numbers,marks)
    percentage= (total_marks/400)*100
    record["Percentage= "]=percentage
    print(record)
    new_student_record.append(record)

    with open("assignment.json","w") as file:
        json.dump(new_student_record, file)

with open("assignment.json","r") as file:
    json_content= json.load(file)

for record in json_content:
    percentage= record["Percentage="]

    if percentage>80:
        print("Distinction")
        disction= disction+1
    elif percentage>=65 or percentage < 80:
        print("Print First division")
        first_division= first_division+1
    elif percentage>=50 or percentage < 65:
        print("Print Second division")
    elif percentage>=40 or percentage < 50:
        print("Print Third division")
    else:
        print("Failed")

    





    