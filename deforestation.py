import pandas as pd
from pandas import DataFrame
import matplotlib.pyplot as plt
import numpy as np

from sklearn.linear_model import LinearRegression

data = pd.read_csv('annual-change-forest-area.csv')


countries = data["Entity"]
numbers = data ["Net forest conversion"]
print(countries)

countryNums1990 = {}
countryNums2000 = {}
countryNums2010 = {}
countryNums2015 = {}

totalList = []
for i in range (0, 474):
    country = countries[i]
    if country == countries[i+1] and i != 473:
        totalList.append(numbers[i])

    else:
        totalList.append(numbers[i])
        if i == 473:
            totalList.append(numbers[i])
        
        if len(totalList) == 4:
            countryNums1990 [country] = totalList[0] 
            countryNums2000 [country] = totalList[0] + totalList[1]
            countryNums2010 [country] = totalList[2] + totalList[0] + totalList[1]
            countryNums2015 [country] = totalList[3] + totalList[2] + totalList[0] + totalList[1]
        elif len(totalList) == 3:
            countryNums1990 [country] = "no data"
            countryNums2000 [country] = totalList[0]
            countryNums2010 [country] = totalList[1] + totalList[2]
            countryNums2015 [country] = totalList[2] + totalList[1] + totalList[0]
        elif len(totalList) == 2:
            countryNums1990 [country] = "no data"
            countryNums2000 [country] = "no data"
            countryNums2010 [country] = totalList[0] 
            countryNums2015 [country] = totalList[1] + totalList[0]
        elif len(totalList) == 1:
            countryNums1990 [country] = "no data"
            countryNums2000 [country] = "no data"
            countryNums2010 [country] = "no data" 
            countryNums2015 [country] = totalList[0] 
        else:
            countryNums1990 [country] = "no data"
            countryNums2000 [country] = "no data"
            countryNums2010 [country] = "no data" 
            countryNums2015 [country] = "no data"

        totalList = []


    






#countries = countries.rest_index()
#totalList = []


    





