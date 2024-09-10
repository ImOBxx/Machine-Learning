import numpy as np
import pandas as pd
import matplotlib.pyplot as plt 

df = pd.read_csv('magic04.csv')

print(df.head(10))

x = df["class"].unique()

print(x)


train, valid, test = np.split(df.sample(frac = 1), [int(0.6 * len(df)), int(0.8 * len(df))])

def scale_dataset(dataframe):
    x = dataframe[dataframe.columns].values
    y = dataframe[dataframe.columns].values

    scaler = StandardScaler()
    x = scaler.fit_transform(x)

    if oversample:
        ros = RandomOverSampler()
        x, y = ros.fit_resample(x, y)

    data = np.hstack((x, np.reshape(y, (-1, 1))))

    return data, x, y 

train, x_train, y_train = scale_dataset(train, oversample = True)


len(y_train)

print(len(train[train["class"] == 1])) #gamma
print(len(train[train["class"] == 0])) #hadron