import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import plotly.graph_objs as go
from sklearn.metrics import confusion_matrix
from sklearn.metrics import r2_score
import plotly.graph_objs as go
from wordcloud import WordCloud
#import geopandas as gpd
from matplotlib.pyplot import figure
from sklearn.metrics import r2_score

data = pd.read_csv('C:/Users/perso/Downloads/modTemp.csv')

x = data.iloc[:,[1,2]].values
y = data.iloc[:,3].values


#KNN
from sklearn.model_selection import train_test_split
x_train,x_test,y_train,y_test = train_test_split(x,y,test_size = 0.1, random_state = 0)
from sklearn.neighbors import KNeighborsClassifier
classifier = KNeighborsClassifier(n_neighbors=3)
classifier.fit(x_train,y_train)
ypred1 = classifier.predict(x_test)
print(r2_score(y_test,ypred1))

from sklearn.svm import SVC
classifier = SVC(kernel = 'rbf', random_state = 0)
classifier.fit(x_train,y_train)
ypred2 = classifier.predict(x_test)
print(r2_score(y_test,ypred2))

#logistic regression
from sklearn.linear_model import LogisticRegression
classifier = LogisticRegression(random_state = 0)
classifier.fit(x_train,y_train)
'predicting output for first value of test set'
ypred3 = classifier.predict(x_test)
print(r2_score(y_test,ypred3))

#randomforest
from sklearn.ensemble import RandomForestClassifier
classifier = RandomForestClassifier(n_estimators = 10, criterion = "gini", random_state = 0)
classifier.fit(x_train, y_train)
ypred4 = classifier.predict(x_test)
print(r2_score(y_test,ypred4))








