        
# from  pandas import read_csv
# from numpy import set_printoptions
# from sklearn import preprocessing


# # data = pd.read_excel(r"C:\Users\amr15\Desktop\AiDataNTI\presidents_names.xlsx")

# # print (data.loc[[1,2],["Name","born"]])

# # data1 = pd.read_csv(r"C:\Users\amr15\Desktop\AiDataNTI\pima-indians-diabetes.csv")
# # print(data1.to_string())
# print("_________________________________________________________________________________________________________ ")



# # data = pd.read_excel(r"C:\Users\amr15\Desktop\AiDataNTI\presidents_names.xlsx")

# # print (data.loc[[1,2],["Name","born"]])

# # data1 = pd.read_csv(r"C:\Users\amr15\Desktop\AiDataNTI\pima-indians-diabetes.csv")
# # print(data1.to_string())
# print("_________________________________________________________________________________________________________ ")


# path = r"C:\Users\amr15\Desktop\AiDataNTI\pima-indians-diabetes.csv"

# names =['prag','plas','pras','skin', 'test','mass','peid', 'age','class']
# dataframe = read_csv(path, names=names)
# array = dataframe.values
# data_scaler = preprocessing.MinMaxScaler(feature_range=(0,1))
# data_rescled = data_scaler.fit_transform(array)

# set_printoptions(precision = 1)

# print ('\n scaled data:\n', data_rescaled[0:5, : ])


import numpy as np
from sklearn import preprocessing

# Input labels
input_labels = ['Embarked', 'Gender']

# Create the label encoder
encoder = preprocessing.LabelEncoder()

# Fit the encoder
encoder.fit(input_labels)

# Transform labels to numeric
encoded_values = encoder.transform(input_labels)
print("\nLabels =", input_labels)
print("Encoded values =", list(encoded_values))

# Inverse transform: convert numbers back to original labels
decoded_1st = encoder.inverse_transform(encoded_values)
print("Decoded labels =", list(decoded_1st))
