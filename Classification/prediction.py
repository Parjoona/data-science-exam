#Naive Bayes classifier
import numpy as np
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.metrics import confusion_matrix
from sklearn.preprocessing import StandardScaler
from sklearn.naive_bayes import GaussianNB
from sklearn.preprocessing import LabelEncoder
from sklearn.neighbors import KNeighborsClassifier

dataset = pd.read_csv('newdataset.csv')

##Vasker facility_zips før det taes i bruk
dataset['newzips'] = np.where(dataset['facility_zip'].str.len() == 5, 
                                   dataset['facility_zip'],
                                   dataset['facility_zip'].str[:5])

'''
proccesed_df = dataset.drop(['serial_number', 'activity_date', 'facility_name', 
                             'grade', 'service_code', 'service_description','facility_address', 'Unnamed: 0', 'employee_id', 'facility_id',
                             'facility_state', 'facility_zip', 'owner_id', 
                             'pe_description', 'program_element_pe', 'program_name', 'program_status', 
                             'facility_city', 'owner_name', 'record_id'], axis = 1)
''' 
# x = Zip Code og År
x = dataset.iloc[:, [21, 24]].values.astype('str')
# Y = Grade
y = dataset.iloc[:, 5].values

le = LabelEncoder()
y = le.fit(y).transform(y)

#Trener opp datasettet
x_train, x_test, y_train , y_test = train_test_split(x, y, test_size= 0.25, random_state = 0)

sc = StandardScaler()
x_train = sc.fit_transform(x_train)
x_test = sc.transform(x_test)


# Creating classifier, training and Predicting the test set results
classifier =  GaussianNB()
classifier.fit(x_train, y_train)
y_pred = classifier.predict(x_test)

cm = confusion_matrix(y_test, y_pred)


'''
y_test = y_test.reshape(-1, 1)

print(classifier.score(y_test, y_pred))
'''