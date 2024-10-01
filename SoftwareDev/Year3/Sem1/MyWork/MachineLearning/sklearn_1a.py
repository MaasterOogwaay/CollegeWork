
from sklearn.tree import DecisionTreeClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import confusion_matrix
from sklearn.metrics import accuracy_score
import pandas as pd

df = pd.read_csv('iris.csv')
df.head()

X = df.drop('species', axis = 'columns')
y = df.species
# for i in range(0,len(y)):
#    print(y[i])
# 125 training and 25 test
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=25,
                                                    random_state=1, stratify=y)
# X_train.pop(X_train[0])
# y_train.pop(y_train[0])
tree = DecisionTreeClassifier()
tree.fit(X_train,y_train)


# Predict the response for test dataset
y_hat = tree.predict(X_test)
print('Here')
print(X_test)
# Model Accuracy, how often is the classifier correct?
print("Accuracy:", accuracy_score(y_test, y_hat))
print("Accuracy2:", tree.score(X_test, y_test))

# confusion matrix
from sklearn.metrics import confusion_matrix
import numpy as np
cm = confusion_matrix(y_test, y_hat)
print(cm)
sum = 0
for num in cm[0]:
    sum += num
res = cm[0][0]/sum
print("Accuracy 1:", int(res*100), "%")
print("now try it for new data")

sepal_length = float(input("Enter septa_length: 4.5-7.1   : "))
sepal_width = float(input("Enter septa_width: 2.8-4.0   : "))
petal_length = float(input("Enter petal_length: 1.1-7.1   : "))
petal_width = float(input("Enter petal_width: 0.1-2.8   : "))
input_data = [[sepal_length, sepal_width, petal_length, petal_width]]

df2 = pd.DataFrame(input_data, columns=['sepal_length',  'sepal_width',  'petal_length',  'petal_width'])
cm_result = tree.predict(df2)
print(cm_result[0])

