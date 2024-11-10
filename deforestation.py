import pandas as pd
from pandas import DataFrame
import matplotlib.pyplot as plt
import numpy as np
import geopandas as gpd
from fuzzywuzzy import process
from shapely.geometry import MultiPolygon
import scipy.stats as stats
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_squared_error, r2_score



data = pd.read_csv('annual-change-forest-area.csv')
worldMap = gpd.read_file('IPUMSI_world_release2024.shp')[['CNTRY_NAME','geometry']]

worldMap.columns = ['Country','geometry']

wCountries = worldMap["Country"]
wGeometry = worldMap["geometry"]



countries = data["Entity"]
numbers = data ["Net forest conversion"]



countryNums1990 = {}
countryNums2000 = {}
countryNums2010 = {}
countryNums2015 = {}

absoluteList = []
relativeList = []
countryList = []
totalList = []
country1990 = []
country2000 = []
country2010 = []
country2015 = []
for i in range (0, 474):
    country = countries[i]
    if country == countries[i+1] and i != 473:
        totalList.append(numbers[i])

    else:
        totalList.append(numbers[i])
        if i == 472:
            totalList.append(numbers[i+1])
        
        if len(totalList) == 4:
            countryNums1990 [country.lower()] = totalList[0] 
            countryNums2000 [country.lower()] = totalList[0] + totalList[1]
            countryNums2010 [country.lower()] = totalList[2] + totalList[0] + totalList[1]
            countryNums2015 [country.lower()] = totalList[3] + totalList[2] + totalList[0] + totalList[1]
        elif len(totalList) == 3:
            countryNums1990 [country.lower()] = 0.0
            countryNums2000 [country.lower()] = totalList[0]
            countryNums2010 [country.lower()] = totalList[1] + totalList[2]
            countryNums2015 [country.lower()] = totalList[2] + totalList[1] + totalList[0]
        elif len(totalList) == 2:
            countryNums1990 [country.lower()] = 0.0
            countryNums2000 [country.lower()] = 0.0
            countryNums2010 [country.lower()] = totalList[0] 
            countryNums2015 [country.lower()] = totalList[1] + totalList[0]
        elif len(totalList) == 1:
            countryNums1990 [country.lower()] = 0.0
            countryNums2000 [country.lower()] = 0.0
            countryNums2010 [country.lower()] = 0.0 
            countryNums2015 [country.lower()] = totalList[0] 
        else:
            countryNums1990 [country.lower()] = 0.0
            countryNums2000 [country.lower()] = 0.0
            countryNums2010 [country.lower()] = 0.0 
            countryNums2015 [country.lower()] = 0.0

        absoluteList.append(totalList[len(totalList) - 1] - totalList[0])
        if totalList[0] != 0:
            relativeList.append(( (totalList[len(totalList) - 1] - totalList[0])/ totalList[0]) * 100)
        else:
            relativeList.append(0)
        countryList.append(country)

        totalList = []

worldList = []
worldList.append(countryNums1990.pop("world"))
worldList.append(countryNums2000.pop("world"))
worldList.append(countryNums2010.pop("world"))
worldList.append(countryNums2015.pop("world"))

valuesDF = pd.DataFrame({
    'Country': countryList,
    'AbsoluteValue': relativeList,
    'RelativeValue': absoluteList
})

df1990= pd.DataFrame.from_dict(countryNums1990,orient = 'index', columns=['Total Forest Cover'])
df1990.reset_index(names=['Country'], inplace=True)

df2000= pd.DataFrame.from_dict(countryNums2000,orient = 'index', columns=['Total Forest Cover'])
df2000.reset_index(names=['Country'],inplace=True)


df2010= pd.DataFrame.from_dict(countryNums2010,orient = 'index', columns=['Total Forest Cover'])
df2010.reset_index(names=['Country'],inplace =True)

df2015= pd.DataFrame.from_dict(countryNums2015,orient = 'index', columns=['Total Forest Cover'])
df2015.reset_index(names=['Country'],inplace = True)

wCountries = worldMap["Country"].str.lower().str.strip()
countries = df2010["Country"].str.lower().str.strip()




countryGeo = {}


#Using the fuzzyWuzzy library for string matching
for i in range (0,len(wCountries)):
    match = process.extractOne(wCountries[i], countries)
    if match and match[1] > 80:  
        countryGeo[match[0]] = wGeometry[i]

newWorldMap= pd.DataFrame.from_dict(countryGeo,orient = 'index', columns=['Geography'])
newWorldMap.reset_index(names=['Country'],inplace = True)

countryMap=(newWorldMap.merge(df2010, on="Country"))





countryMap = gpd.GeoDataFrame(countryMap, geometry='Geography')


countryMap = countryMap.set_crs("EPSG:4326")

'''

def changeToMultipolygon(geom):
    if geom.geom_type == 'Polygon':
        return MultiPolygon([geom])
    elif geom.geom_type == 'MultiPolygon':
        return geom
    else:
        return None

    


countryMap['geometry'] = countryMap['Geography'].apply(changeToMultipolygon)
countryMap = countryMap.dropna(subset=['geometry'])
'''

print(countryMap)

specific_data = countryMap.loc[countryMap['Country'] == 'brazil']
brazil_geometry = specific_data['Geography'].values[0]
print(brazil_geometry)

title = 'Deforestation Rate'
column = 'Total Forest Cover'
source = "Source: https://ourworldindata.org/deforestation"
vmin = countryMap[column].min()
vmax = countryMap[column].max()
cmap = 'cool'

fig, ax = plt.subplots(1, figsize=(20, 8))
ax.axis('off')
countryMap.plot(column=column, ax=ax, linewidth=1, cmap=cmap, edgecolor = '0.8')

ax.set_title(title, fontdict={'fontsize': '25', 'fontweight': '3'})

ax.annotate(source, xy=(0.1, .08), xycoords='figure fraction', horizontalalignment='left', 
            verticalalignment='bottom', fontsize=10)
            

sm = plt.cm.ScalarMappable(norm=plt.Normalize(vmin=vmin, vmax=vmax), cmap=cmap)

sm.set_array([])


cbaxes = fig.add_axes([0.15, 0.25, 0.01, 0.4])
cbar = fig.colorbar(sm, cax=cbaxes)

plt.show()



'''
totalList = []
totalList.append(worldList[0])
totalList.append(worldList[0]+worldList[1])
totalList.append(worldList[0]+ worldList[1]+ worldList[2])
totalList.append(worldList[0]+ worldList[1]+ worldList[2] + worldList[3])
x = [1990,2000,2010,2015]

X = np.array(x).reshape(-1, 1)  
y = np.array(totalList) 


X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

slope, intercept, r, p, std_err = stats.linregress(x, totalList)

if r> 0.7 or r< -0.7:

    model = LinearRegression()
    model.fit(X, y)

    y_pred = model.predict(X_test)

    X.reshape(-1,1)
    X_future = np.array(range(2015, 2031)).reshape(-1,1)
    y_future = model.predict(X_future)

    plt.scatter(X, y, color='blue')  
    plt.plot(X, model.predict(X), color='red', linewidth=2) 

    plt.scatter(X_future, y_future, color = "green")
    plt.plot(X_future, y_future, color = "red")

    plt.title("Linear Regression Example")
    plt.xlabel("Year")
    plt.ylabel("Forest Area (hectares)")
    plt.show()

brazilTotals = []
brazilTotals.append(countryNums1990['brazil'])
brazilTotals.append(countryNums2000['brazil'])
brazilTotals.append(countryNums2010['brazil'])
brazilTotals.append(countryNums2015['brazil'])

totalList = []
totalList.append(brazilTotals[0])
totalList.append(brazilTotals[0]+brazilTotals[1])
totalList.append(brazilTotals[0]+ brazilTotals[1]+ brazilTotals[2])
totalList.append(brazilTotals[0]+ brazilTotals[1]+ brazilTotals[2] + brazilTotals[3])
x = [1990,2000,2010,2015]

X = np.array(x).reshape(-1, 1)  
y = np.array(totalList) 


X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

slope, intercept, r, p, std_err = stats.linregress(x, totalList)

print(r)

if r> 0.7 or r< -0.7:

    model = LinearRegression()
    model.fit(X_train, y_train)

    y_pred = model.predict(X_test)

    X.reshape(-1,1)
    X_future = np.array(range(2015, 2031)).reshape(-1,1)
    y_future = model.predict(X_future)

    plt.scatter(X, y, color='blue')  
    plt.plot(X, model.predict(X), color='red', linewidth=2) 

    plt.plot(X_future, y_future, color = "green")

    plt.title("Brazil Prediction")
    plt.xlabel("Year")
    plt.ylabel("Forest Area (hectares)")
    plt.show()
else: 
    print("BBBBBBBBB")

'''


    





