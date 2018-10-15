from sklearn import svm
import pickle
from sklearn.externals import joblib 

print('Training the SVM classifier......')

with open('./trackdata1133.pickle', 'rb') as file:
    data_dict = pickle.load(file)
    x_train = data_dict['x_train']
    x_test = data_dict['x_test']    
    y_train = data_dict['y_train']
    y_test = data_dict['y_test']

clf = svm.SVC()
clf.fit(x_train, y_train)
score = clf.score(x_train, y_train)
print("train score:", score)

## save the model
joblib.dump(clf, "./models/svm_normal_uniformmap1133.m")

## evaluate the model

test_predict = clf.predict(x_test)

print("valid score:", clf.score(x_test, y_test))