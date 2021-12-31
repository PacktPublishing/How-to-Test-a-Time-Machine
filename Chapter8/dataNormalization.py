import datetime
import pandas as pd
# Retrieve the test cases from the csv into a dictionary
dataFile = open('testcases.csv', 'r')
dataFrame = pd.read_csv('testcases.csv', index_col=0)
dataDictionary = dataFrame.transpose().to_dict()
# Create a new dictionary to save the results
result = {}
# Data optimization -> get the maximum number of steps and of differences
oldest = 0
maxSteps = 0
for i in dataDictionary:
    createdDate = datetime.datetime.fromisoformat(dataDictionary[i]['CreatedDate'])
    currentDate = datetime.datetime.now()
    difference = currentDate - createdDate
    daysOfDifference = difference.days
    dataDictionary[i]['daysDiff'] = daysOfDifference
    if daysOfDifference > oldest:
        oldest = daysOfDifference
    if dataDictionary[i]['Steps'] > maxSteps:
        maxSteps = dataDictionary[i]['Steps']
# Save the data in the new dictionary
for i in dataDictionary:
        result[i] = {}
        passes = dataDictionary[i]['passes']
        fails = dataDictionary[i]['fails']
        # Data optimization - get the percentage of passes
        passingTest = (passes / (fails + passes)) * 100
        # Data optimization - get the percentage of test age
        testAge = (dataDictionary[i]['daysDiff'] / oldest) * 100
        priorityTest = dataDictionary[i]['Priority']
        # Data optimization - get the percentage of number steps
        numSteps = (dataDictionary[i]['Steps'] / maxSteps) * 100
        # Save the new values
        result[i]['Priority'] = float(priorityTest)
        result[i]['Age'] = float(testAge)
        result[i]['Steps'] = float(numSteps)
        result[i]['Passing'] = float(passingTest)
        result[i]['Expected'] = float(dataDictionary[i]['LastResult'])
# Data normalization
from sklearn.preprocessing import StandardScaler 
# retrieve data from previous chapter as above  
sc = StandardScaler() 
dataFrameResult = pd.DataFrame.from_dict(result, orient='index')
# Curating the data of the rest of the variables 
dataFrameResult[['Age', 'Steps', 'Passing']] = sc.fit_transform(dataFrameResult[['Age', 'Steps', 'Passing']]) 
# Save to the new Data File
dataFile = open('newDataBoth.csv', 'w')
dataFrameResult.to_csv(dataFile, sep=',')
dataFile.close()