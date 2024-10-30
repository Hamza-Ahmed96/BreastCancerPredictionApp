
import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib as plt
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.metrics import accuracy_score, classification_report
import pickle as pk

# function to train model and retrun the model and scaler 
def create_model(data, verbose=False):
    # get features 
    X = data.drop('diagnosis', axis=1)
    y = data['diagnosis']
    # standardise the data set:
    scaler = StandardScaler()
    X = scaler.fit_transform(X)
    
    # Create test train split
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=529)
    
    # train the model :
    lr = LogisticRegression()
    model = lr.fit(X_train, y_train)
    
    # predict and reports
    y_pred = model.predict(X_test)
    
    model_accuracy = accuracy_score(y_pred=y_pred, y_true=y_test)
    model_classificaiton = classification_report(y_pred=y_pred, y_true=y_test)
    if verbose:
        print(f'Model accuracy : {model_accuracy}')
        print(f'Classification Report: {model_classificaiton}')
        
    return model, scaler
          
#  Function to drop any null values and to one-shot-encode the target labels
def get_clean_data():
    # read the data into a pandas data frame
    data = pd.read_csv('data/data.csv')
    # remove null values:
    data = data.dropna(axis = 1)
    # rename the Target Lables from Malignant to 1 and Benign to 0
    data['diagnosis'] = data['diagnosis'].map({'M': 1, 'B':0})
    
    return data
    
def main():
    clean_data = get_clean_data()
    model, scaler = create_model(clean_data, False)
    
    with open('model/model.pkl', 'wb') as file:
        pk.dump(model, file)
        
    with open('model/scaler.pkl', 'wb') as file:
        pk.dump(scaler, file)
        
    
    
        
if __name__ == '__main__':
    main()