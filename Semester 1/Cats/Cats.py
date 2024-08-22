#!/usr/bin/env python
# coding: utf-8

# In[ ]:


#imports
import pandas as pd
import sys
import os
import time
import matplotlib.pyplot as plt


# In[ ]:


#Set Data File & affirm
dfaffirm = input("what csv do you want? 1: cats.csv")
if dfaffirm == '1':
    df = pd.read_csv('cats.csv')
    print("cats.csv imported successfully")
    df.drop(['Unnamed: 0'], inplace=True, axis=1)
else:
    try:
        df = pd.read_csv(dfaffirm)
        if df == pd.read_csv(dfaffirm):
            print(dfaffirm, "imported successfully")
            time.sleep(2)
    except:
        print('An error ocurred with the import. Are you sure the file is present?')
        input('Aborting...')
        try:
            raise SystemExit
        except:
            print("system exit failed. This is a problem")
            try:
                os._exit(0)
            except:
                print("os exit also failed. This is a really big problem")
                try:
                    quit()
                except:
                    print("even quit failed. please contact charred baguette about this")


# In[ ]:





# In[ ]:


#give basic options
while True:
    Columns = df.columns
    print("1: Print Columns")
    print("2: Print first # values")
    print("3: Print last # values")
    print("4: give basic stats of the data frame")
    print("5: create a plot")
    print("6: specific sample description")
    print("7: drop a column")
    print("8: add a new row")
    print("9: clear screen")
    print("10: check the kind of data a column is")
    print("exit")
    req = input("please select function:")
    
    if req == '1':
        #print columns 
        print("columns:",list(Columns))
        time.sleep(2)

    
    elif req =='2':
        number = int(input("amount of values?"))
        print(df.head(number))
        time.sleep(2)

    
    elif req =='3':
        number = int(input("amount of values?"))
        print(df.tail(number))
        time.sleep(2)

    
    elif req =='4':
        print(df.describe())
        time.sleep(2)

    
    elif req =='5':
        while True:
            print("1: line plot")
            print("2: Scatterplot")
            print("3: histogram")
            print("4: exit")
            plot = input("Which plot type?")
            if plot == '1':
                try:
                    print("Columns:",list(Columns))
                    NumcolmnX = input("which numeric column for the x axis?")
                    NumcolmnY = input("which numeric column for the y axis?")
                    if NumcolmnX not in Columns:
                        print("Column X doesn't exist")
                        time.sleep(2)
                    elif NumcolmnY not in Columns:
                        print("Column Y doesn't exist")
                        time.sleep(2)
                    elif df[NumcolmnX].dtype == 'object':
                        print(NumcolmnX, "is an object, not numeric")
                        time.sleep(2)
                    elif df[NumcolmnY].dtype == 'object':
                        print(NumcolmnY, "is an object not a numeric")
                        time.sleep(2)
                    else:
                        df.plot(x=NumcolmnX, y=NumcolmnY)
                        plt.xlabel(NumcolmnX)
                        plt.ylabel(NumcolmnY)
                        plt.title(f'Line Plot of {NumcolmnX} vs {NumcolmnY}')
                        plt.show()
                    time.sleep(2)
                except:
                    print("There was an unexpected issue.")
                time.sleep(2)
            elif plot == '2':
                try:
                    print("Columns:",list(Columns))
                    NumcolmnX = input("which column for the x axis?")
                    NumcolmnY = input("which column for the y axis?")
                    if NumcolmnX not in Columns:
                        print("Column X doesn't exist")
                        time.sleep(2)
                    elif NumcolmnY not in Columns:
                        print("Column Y doesn't exist")
                        time.sleep(2)
                    else:
                        df.plot.scatter(x=NumcolmnX, y=NumcolmnY)
                        plt.xlabel(NumcolmnX)
                        plt.ylabel(NumcolmnY)
                        plt.title(f'Scatter Plot of {NumcolmnX} vs {NumcolmnY}')
                        plt.show()
                        time.sleep(2)
                except:
                    print("There was an unexpected issue.")
                time.sleep(2)
            elif plot =='3':
                try:
                    print("Columns:",list(Columns))
                    NumcolmnX = input("which column for the x axis?")
                    NumcolmnY = input("which column for the y axis?")
                    if NumcolmnX not in Columns:
                        print("Column X doesn't exist")
                        time.sleep(2)
                    elif NumcolmnY not in Columns:
                        print("Column Y doesn't exist")
                        time.sleep(2)
                    else:
                        if df[NumcolmnX].dtype == 'object':
                            print(NumcolmnX, "is an object, not numeric")
                            print("this will make the histogram display the count/frequency of the unique values")
                            time.sleep(2)
                        if df[NumcolmnY].dtype == 'object':
                            print("you cannot have the Y axis be an object")
                            break
                        try:
                            df.plot.hist(x=NumcolmnX, y=NumcolmnY)
                            plt.xlabel(NumcolmnX)
                            plt.ylabel(NumcolmnY)
                            plt.title(f'Histogram of {NumcolmnX} vs {NumcolmnY}')
                            plt.show()
                        except:
                            print("there was an unexpected error with the plotting.")
                        time.sleep(2)
                except:
                    print("There was an unexpected issue.")
                    time.sleep(2)
            elif plot=='4':
                break
            time.sleep(2)

    
    elif req=='6':
        sample = int(input("which sample/index?"))
        sampleref = sample-1
        specs=df.loc[sampleref]
        print(specs)
        time.sleep(2)

    
    elif req=='7':
        Type=input("drop a column or row?")
        try:
            if Type =='column':
                print("Columns:",list(Columns))
                drop=input("what do you want to drop?")
                df.drop([drop], inplace=True, axis=1)
            elif Type =='row':
                df.drop([drop], inplace=True, axis=0)
                drop=input("what do you want to drop?")
            else:
                print("please specify a column or row")
        except:
            print("unexpected error")
        time.sleep(2)

    
    elif req=='8':
        print("Columns:",list(Columns))
        new_row = {}
        for column in Columns:
            new_row[column] = input(f"enter value for column '{column}':")
        row = pd.DataFrame([new_row], columns=Columns)
        df = pd.concat([df, row], ignore_index=True)
        time.sleep(2)

    
    elif req=='9':
        if os.name=='nt':
            os.system('cls')
        else:
            os.system('cls')

    
    elif req =='10':
        print("columns:",list(Columns))
        Check=input("what column do you want to check the type of?")
        print(df[Check].dtype)
        time.sleep(2)

    #cats.csv specific testing option
    elif req =='99':
        zuko = pd.DataFrame({'Breed': 'tabby', 'Age (Years)': 3, 'Weight (kg)': 5, 'Color': 'orange', 'Gender': 'male'}, index=[0])
        df = pd.concat([df, zuko], ignore_index=True)
        print(df)
        time.sleep(2)

    #cats.csv specific testing option
    elif req =='100':
        df['weight (lbs)'] = df['Weight (kg)'] * 2.205
        print(df.tail())
        time.sleep(2)

    
    elif req =='exit':
        print("have a good rest of your day!")
        time.sleep(.5)
        break
        raise SystemExit


# In[ ]:





# ##### 

# In[ ]:





# In[ ]:




