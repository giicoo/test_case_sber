import pandas as pd
import numpy as np
from prepare import prepare

def mini_ml(X, y):
    w = np.zeros(X.shape[1]) 
    b = 0.0

    epochs = 1000
    learning_rate = 0.00000001  
    m = X.shape[0]  

    for i in range(epochs):
        y_pred = X @ w + b  
        error = y_pred - y  
        
        dw = (2/m) * X.T @ error  
        db = (2/m) * np.sum(error)

        w -= learning_rate * dw
        b -= learning_rate * db

    y_pred_final = X @ w + b


    mse = 1/m*np.sum((y_pred_final-y) ** 2)

    print(f"w={w}, b={b}, MSE={mse}")


df = prepare()

year = df["year"].to_numpy()
runtime = df["runtime"].dt.total_seconds()
rating = df["rating"].to_numpy()

X = np.column_stack((year, runtime)) 
y = rating 

mini_ml(X, y)