import pandas as pd 

data1 = pd.read_csv(r"C:\Users\amr15\Desktop\AiDataNTI\data.csv")

print(data1.to_string())
print("_________________________________________________________________________________________________________ ")
print(data1.head(10))
print("_________________________________________________________________________________________________________ ")
data1.dtypes
print(data1.dtypes)
print("_________________________________________________________________________________________________________ ")
print(data1.info)
print("_________________________________________________________________________________________________________ ")
data1['Precentage']= data1 ['Precentage'].str.strip("%")
print(data1.head(10))
print("_________________________________________________________________________________________________________ ")
DataSumOfDuration = data1["Duration"].sum()
print( "SumOfDuration = ",DataSumOfDuration)
print("_________________________________________________________________________________________________________ ")
DataSumOfCalories = data1["Calories"].sum()
print( "SumOfCalories = ",DataSumOfCalories)
print("_________________________________________________________________________________________________________ ")
assert data1 ['Pulse'].dtype == 'int'
print("_________________________________________________________________________________________________________ ")
Data1Describe = data1['Maxpulse'].describe()
print(Data1Describe)
print("_________________________________________________________________________________________________________ ")
# import matplotlib.pyplot as plt

# plt.hist(data1["Maxpulse"], bins=10, color='skyblue', edgecolor='black')
# plt.title("Distribution of Maxpulse")
# plt.xlabel("Maxpulse")
# plt.ylabel("Frequency")
# plt.grid(True)
# plt.show()
# print("_________________________________________________________________________________________________________ ")
DataTest = pd.read_csv(r"C:\Users\amr15\Desktop\AiDataNTI\Test.csv")
print(DataTest.to_string())
Data1RAtingMoreThen40 =DataTest.drop(DataTest[DataTest['ORDERLINENUMBER']>5].index , inplace = False)
print(Data1RAtingMoreThen40)
print("_________________________________________________________________________________________________________ ")

# convertRatingForDataTest = DataTest.loc[DataTest["Rating"]>5],'Rating'=5
# print(convertRatingForDataTest)

print("_________________________________________________________________________________________________________ ")
 