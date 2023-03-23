import pandas as pd
dataFrame = pd.read_csv('doc.csv', index_col=0)
dataDictionary = dataFrame.transpose().to_dict()