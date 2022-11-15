# Data normalization
from sklearn.preprocessing import StandardScaler
import pandas as pd
import datetime
import time
# Retrieve the test cases from the csv 
dataFile = open('testcases.csv', 'r')
dataFrame = pd.read_csv('testcases.csv', index_col=0)
sc = StandardScaler() 
# Curating the data of the rest of the variables
# Note - passing should be input manually in this case, or automated as above / created date should be in timestamp
dataFrame['CreatedDate'] = [datetime.datetime.fromisoformat(t).timestamp() for t in dataFrame['CreatedDate']]
dataFrame['Passing'] =dataFrame['passes'] / (dataFrame['passes'] + dataFrame['fails'] )
dataFrame[['CreatedDate', 'Steps', 'Passing']] = sc.fit_transform(dataFrame [['CreatedDate', 'Steps', 'Passing']])
# Save to the new Data File
#dataFrame = pd.DataFrame.from_dict(dataFrame.columns, orient='index')
dataFile = open('newDataSKLearn.csv', 'w')
dataFrame.to_csv(dataFile, sep=',')
dataFile.close()