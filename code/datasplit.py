import numpy as np
import pandas as pd
from sklearn.cross_validation import train_test_split
import sys

def load_raw_data(path):
    input = pd.read_csv(path)
    return input
def split(Input, Oversample = 1):
    Input_1 = Input[Input["default"] ==1] 
    Input_0 = Input[Input["default"] == 0]
    Input_1_train_valid, Input_1_test = train_test_split(Input_1, test_size = 0.2)
    Input_0_train_valid, Input_0_test = train_test_split(Input_0, test_size = 0.05)
    Input_train_valid = Input_0_train_valid
    for i in range(Oversample):
        Input_train_valid = Input_train_valid.append(Input_1_train_valid)
    Input_train_valid = Input_train_valid.sample(frac = 1)
    Input_train, Input_valid = train_test_split(Input_train_valid, test_size = 0.2)
    Input_test = Input_0_test.append(Input_1_test)
    Input_test = Input_test.sample(frac = 1)
    train_y = Input_train["default"]
    train_X = Input_train.drop(columns = ["default"])
    valid_y = Input_valid["default"]
    valid_X = Input_valid.drop(columns = ["default"])
    test_y = Input_test["default"]
    test_X = Input_test.drop(columns = ["default"])
    print("training sample number is :"+str(train_X.shape[0]))
    print("validation sample number is : "+str(valid_X.shape[0]))
    print("testing sample number is ： " +str(test_X.shape[0]))
    return train_X, train_y, valid_X, valid_y, test_X, test_y

def get_name(variable):
    for k, v in list(locals().items()):
         if v is variable:
             name_as_str = k
    return name_as_str
def write (train_X,train_y, valid_X, valid_y, test_X, test_y):
    train_X.to_csv("../intermidiate_data/train_X.csv", index = False)
    train_y.to_csv("../intermidiate_data/train_y.csv", index = False)
    valid_X.to_csv("../intermidiate_data/valid_X.csv", index = False)
    valid_y.to_csv("../intermidiate_data/train_y.csv", index = False)
    test_X.to_csv("../intermidiate_data/test_X.csv", index = False)
    test_y.to_csv("../intermidiate_data/test_y.csv", index = False)
    
def main():
    input = load_raw_data(sys.argv[1])
    train_X,train_y, valid_X, valid_y, test_X, test_y = split(input)
    write(train_X,train_y, valid_X, valid_y, test_X, test_y)
    print("done")
if __name__ == "__main__":
    main()
