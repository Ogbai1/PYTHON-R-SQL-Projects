import pandas as pd
import numpy as np

# create csv file in read mode
df=pd.read_csv(r"C:\Users\user\Desktop\Test\Holiday_Destins.csv") 
print(df)

#Create dictionary that enables to add in a column of destinations, feedback score, number of all-incluve hotels and most visited city  
destinations={'Dest_country':["Spain", "Turkey", "Spain", "Costa_rica", "Arab-Imirates","Greece", "South_Africa", "USA","Malta","USA","Kenya","USA","USA","Japan","France"],'Score':[1.0,1.5,2.0,2.5,3.0,3.5,4.0,4.5,5.0,5.5,6.0, 6.5,7.0,7.5,8.0],'Star_rating':[15,14,13,12,11,9,10,8,7,5,6,3,4,1,2],'Number_hotels':[80,20,30,150,110,70,80,90,120,90,50,130,70,40,60],'Most_visited':["Barcelona","Istanbul", "Canary_Islands","Sanjose", "Dubai","Athens","Cape_Town","Las_Vegas" ,"Malta","Miami","Nairobi","New_York","Orlando","Osaka","Paris"]}
df=pd.DataFrame(destinations)
print(df) 

 #to print the star rating 




# Alternative to the above, using for-loop by decreasing star rating by -1
for i in range (15):
    for j in range(i-1):
        print('*',end='')
        print()

# 6 rows x 15 columns are set up to make the dataframe

# The alternative way of creating dataframe has been used to locate row 3-8 using loc 

# Find thee mean number of all-inclusive hotels
from numpy import mean
number_hotels = [80,20,30,150,110,70,80,90,120,90,50,130,70,40,60]
avg = mean(number_hotels)
print("The average of List is ", round(avg, 2))
#Output 
# The average of List is  79.33
#Find highest Scoring destination and lowest scoring destination

import numpy
Score1=[1.0,1.5,2.0,2.5,3.0,3.5,4.0,4.5,5.0,5.5,6.0, 6.5,7.0,7.5,8.0]
max_element = numpy.max(Score1)
min_element = numpy.min(Score1)
print("The highest scoring destination is: ", max_element)
print("The lowest scoring destination is: ", min_element)

#Find all the destinations where there are more than 9 all inclusive hotels.
df.loc[lambda df: df['Number_hotels'] > 9]=0

#Filter the data by score above 8 and below 2
import pandas as pd
data=pd.read_csv(r"C:\Users\user\Desktop\Test\Holiday_Destins.csv")
data[(data.Score>8 & data.Score<2)]
print('the values prove', data)

#correlation between number of all inclusive hotels and score? 
df=pd.read_csv(r"C:\Users\user\Desktop\Test\Holiday_Destins.csv") 
print(df)
y=df['Number_hotels']
x=df['Score']
correlation = x.corr(y)
print('There is very low positive correlation', correlation)

#Output for the above code is 0.166035 Thus both factors have very weak correlation nearly to 0.   

#Visualisation 
df=pd.read_csv(Holiday_Destins.csv)
df.plot(x='Destin_Country',y='Score')