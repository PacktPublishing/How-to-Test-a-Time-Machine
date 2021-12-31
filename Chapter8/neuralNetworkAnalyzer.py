from sklearn.model_selection import train_test_split
import pandas as pd

# Retrieve the test cases from the csv into a dictionary
dataFile = open('newDataBoth.csv', 'r')
dataFrame = pd.read_csv('newDataBoth.csv', index_col=0)
# saving the expected data as a target - we prepare it for later processing
target_col = ['Expected'] 
# Adding the variables into their own grid for later use - for later processing
variables = list(set(list(dataFrame.columns))-set(target_col))
print(variables)
print('---------------------------')
print(dataFrame[variables])
# Creating training and test datasets
X = dataFrame[variables].values
# using ravel to transform to array
y = dataFrame[target_col].values.ravel()
X_train, X_test, y_train, y_test = train_test_split(X, y, stratify=y, test_size=0.05, random_state=42)

# Training the system
from sklearn.neural_network import MLPClassifier
classifier = MLPClassifier(hidden_layer_sizes=(400, 200, 100), activation='relu', solver='adam', max_iter=300, random_state=42)
classifier.fit(X_train, y_train)
predict_train = classifier.predict(X_train)
predict_test = classifier.predict(X_test)

# Analyzing the data on the train model
from sklearn.metrics import confusion_matrix, classification_report
print(confusion_matrix(y_train, predict_train))
print(classification_report(y_train, predict_train))
# Analyzing the data on the test model
print(confusion_matrix(y_test, predict_test))
print(classification_report(y_test, predict_test))

# Check the second [] at the top left and the f1-score of 1 (passing)