#!/usr/bin/env python
# coding: utf-8

# In[ ]:


#necessary imports
import random
import csv
import datetime
import time




# In[ ]:


print("This is a random dataset generator. It will produce a .csv")


# In[ ]:


#Basic questions
rows=int(input("how many rows do you want?"))
columns=int(input("how many columns do you want?"))


# In[ ]:


#ask different column names
cats=[]
num=[]
for i in range(columns):
    cat=input(f"what column do you want for column{i}")
    cats.append(cat)
    nmafrm=input(f"do you want {cat} to be numeric? Yes or n")
    if nmafrm == 'yes' or nmafrm=='Yes' or nmafrm=='y':
        num.append(i)
        print(f"cat{i} will be numeric")
    else:
        print(f"{cat} will not be numeric")
print(f"these are your columns: {cats}")
print(f"these are the numeric columns: {[cats[i] for i in num]}")


# In[ ]:


#numeric columns
fin=[[] for i in range(rows)]

print("will now start populating numeric columns")

max=int(input("what is the max possible number you want?"))
min=int(input("What is the min possible number you want?"))

for row in range(rows):
    for col in range(columns):
        if col in num:
            v = random.randint(min, max)
            fin[row].append(v)
            print(f"{cats[col]}, row: {row}, value: {v}")
        else:
            fin[row].append("")
for row in fin[:2]:
    print(row)


# In[ ]:


#non-numeric
print("will now start populating non-numeric columns")
for row in range(rows):
    for col in range(columns):
        if col not in num:
            print("Active column:", col, "Active Row:", row)
            print("1: Random name")
            print("2: Random date")
            print("3: Random color")
            print("4: Random of your choice")
            choice=input("what is your choice?(1-4)")
            if choice =='1':
                names=['Liam', 'Olivia', 'Noah', 'Emma', 'Oliver', 'Ava', 'Elijah', 'Charlotte', 'William', 'Sophia', 'James', 'Amelia', 'Benjamin', 'Isabella', 'Lucas', 'Mia', 'Henry', 'Evelyn', 'Alexander', 'Harper','Mason', 'Camila', 'Michael', 'Gianna', 'Ethan', 'Abigail', 'Daniel', 'Luna', 'Jacob', 'Ella',
         'Logan', 'Elizabeth', 'Jackson', 'Sofia', 'Sebastian', 'Emily', 'Jack', 'Avery', 'Aiden', 'Mila',
         'Owen', 'Scarlett', 'Samuel', 'Eleanor', 'Matthew', 'Madison', 'Joseph', 'Layla', 'Levi', 'Penelope',
         'Mateo', 'Aria', 'David', 'Chloe', 'John', 'Grace', 'Wyatt', 'Ellie', 'Carter', 'Nora',
         'Julian', 'Hazel', 'Luke', 'Zoey', 'Grayson', 'Riley', 'Isaac', 'Victoria', 'Jayden', 'Lily',
         'Theodore', 'Aurora', 'Gabriel', 'Violet', 'Anthony', 'Nova', 'Dylan', 'Hannah', 'Leo', 'Emilia',
         'Lincoln', 'Zoe', 'Jaxon', 'Stella', 'Asher', 'Everly', 'Christopher', 'Isla', 'Josiah', 'Leah',
         'Andrew', 'Lillian', 'Thomas', 'Addison', 'Joshua', 'Willow', 'Ezra', 'Lucy', 'Hudson', 'Paisley',
         'Charles', 'Natalie', 'Caleb', 'Naomi', 'Isaiah', 'Eliana', 'Ryan', 'Brooklyn', 'Nathan', 'Elena',
         'Adrian', 'Aubrey', 'Christian', 'Claire', 'Maverick', 'Ivy', 'Colton', 'Kinsley', 'Elias', 'Audrey',
         'Aaron', 'Maya', 'Eli', 'Genesis', 'Landon', 'Skylar', 'Jonathan', 'Bella', 'Nolan', 'Aaliyah',
         'Hunter', 'Madelyn', 'Cameron', 'Savannah', 'Connor', 'Anna', 'Santiago', 'Delilah', 'Jeremiah', 'Serenity',
         'Ezekiel', 'Caroline', 'Angel', 'Kennedy', 'Roman', 'Valentina', 'Easton', 'Ruby', 'Miles', 'Sophie']
                fin[row][col]=random.choice(names)

            elif choice=='2':
                sd=datetime.datetime(1900,1,1)
                ed=datetime.datetime.now()
                rd=sd+datetime.timedelta(days=random.randint(0, (ed - sd).days))
                fin[row][col]=rd.strftime('%y-%m-%d')

            elif choice=='3':
                fin[row][col]=random.choice(['Red', 'Blue', 'Green', 'Yellow', 'Purple', 'Orange', 'Pink', 'Brown', 'Gray', 'Black', 'Navy'])
            elif choice=='4':
                choices=input("what are thy choices (seperate them with commas!):").split(',')
                fin[row][col]=random.choice(choices)
            else:
                print("invalid input so invalid will be placeholder")
                fin[row][col]=("invalid")


# In[ ]:


#final check
prev=int(input("how many rows do you want to preview?"))
for row in fin[:prev]:
    print(row)


# In[ ]:


#save

ultraconfirm=input("do you want to save this?")
if ultraconfirm=='yes' or ultraconfirm=='YES' or ultraconfirm=='Yes' or ultraconfirm=='y':
    finalpathname=input("what do you want to name it? Please include .csv")
    with open(finalpathname, 'w', newline='') as file:
        csv.writer(file).writerow(cats)
        csv.writer(file).writerows(fin)
    print("your data has been written as", finalpathname)
else:
    print("data not saved")
    time.sleep(1)
    


# In[ ]:




