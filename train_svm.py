from sklearn import svm
import pickle
from sklearn.externals import joblib 

with open('././train_data/train_for_classifier_uniform_area.pickle', 'rb') as file:
    data_dict = pickle.load(file)
    x_train = data_dict['x_train']
    x_test = data_dict['x_test']    
    y_train = data_dict['y_train']
    y_test = data_dict['y_test']

print('Training the SVM classifier......')
clf = svm.SVC()
clf.fit(x_train, y_train)
score = clf.score(x_train, y_train)
print("train score:", score)

## save the model
joblib.dump(clf, "./models/svm_normal_uniformmap.m")

## evaluate the model

test_predict = clf.predict(x_test)

print(clf.score(x_test, y_test))