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
for data in dataDictionary:
    createdDate = datetime.datetime.fromisoformat(dataDictionary[data]['CreatedDate'])
    currentDate = datetime.datetime.now()
    difference = currentDate - createdDate
    daysOfDifference = difference.days
    dataDictionary[data]['daysDiff'] = daysOfDifference
    if daysOfDifference > oldest:
        oldest = daysOfDifference
    if dataDictionary[data]['Steps'] > maxSteps:
        maxSteps = dataDictionary[data]['Steps']
# Save the data in the new dictionary
for data in dataDictionary:
        result[data] = {}
        passes = dataDictionary[data]['passes']
        fails = dataDictionary[data]['fails']
        # Data optimization - get the percentage of passes
        passingTest = (passes / (fails + passes)) * 100
        # Data optimization - get the percentage of test age
        testAge = (dataDictionary[data]['daysDiff'] / oldest) * 100
        priorityTest = dataDictionary[data]['Priority']
        # Data optimization - get the percentage of number steps
        numSteps = (dataDictionary[data]['Steps'] / maxSteps) * 100
        # Save the new values
        result[data]['Priority'] = float(priorityTest)
        result[data]['Age'] = float(testAge)
        result[data]['Steps'] = float(numSteps)
        result[data]['Passing'] = float(passingTest)
        result[data]['Expected'] = float(dataDictionary[data]['LastResult'])
# Save to the new Data File
dataFrame = pd.DataFrame.from_dict(result, orient='index')
dataFile = open('newData.csv', 'w')
dataFrame.to_csv(dataFile, sep=',')
dataFile.close()
