import pandas as pd
import numpy as np 
import sklearn
#from sklearn import linear model 
from sklearn.utils import shuffle 

data = pd.read_csv("student-mat.csv", sep=";")

print (data)


data = data[["G1" , "G2" , "G3" , "studytime" , "failures" , "absences"]]

