import pickle

with open('../trackdata1133.pickle', 'rb') as file:
    data_dict = pickle.load(file)
    x_train = data_dict['x_train']
    x_test = data_dict['x_test']    
    y_train = data_dict['y_train']
    y_test = data_dict['y_test']

data_1 = {'x_train': x_train[:250000], 'y_train': y_train[:250000]}
with open('./trackdata1133_1.pickle','wb') as file:
	pickle.dump(data_1, file)

data_2 = {'x_train': x_train[250000:500000], 'y_train': y_train[250000:500000]}
with open('./trackdata1133_2.pickle','wb') as file:
	pickle.dump(data_2, file)

data_3 = {'x_train': x_train[500000:750000], 'y_train': y_train[500000:750000]}
with open('./trackdata1133_3.pickle','wb') as file:
	pickle.dump(data_3, file)

data_4 = {'x_train': x_train[750000:], 'y_train': y_train[750000:]}
with open('./trackdata1133_4.pickle','wb') as file:
	pickle.dump(data_4, file)

data_5 = {'x_test': x_test[:250000], 'y_test': y_test[:250000]}
with open('./trackdata1133_5.pickle','wb') as file:
	pickle.dump(data_5, file)

data_6 = {'x_test': x_test[250000:], 'y_test': y_test[250000:]}
with open('./trackdata1133_6.pickle','wb') as file:
	pickle.dump(data_6, file)