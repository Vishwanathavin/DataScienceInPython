import pandas as pd
from sklearn import linear_model
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_squared_error, r2_score
import matplotlib.pyplot as plt

inpData = pd.read_csv('../Data/linearReg.txt', sep=",", header=None)
inpData.columns = ["area", "bedroom", "Rate"]

X=inpData.drop('Rate',axis=1)
y=inpData['Rate']
#
# X=(X - X.mean()) / (X.max() - X.min())

X_train,X_test,Y_train,Y_test= train_test_split(X, y, test_size=0.33, random_state=42)

print X_train.shape
print X_test.shape
print Y_train.shape
print Y_test.shape

regModel = linear_model.LinearRegression(fit_intercept=False, normalize=True)
regModel.fit(X_train, Y_train)

Y_pred = regModel.predict(X_test)


# The coefficients
print('Coefficients: \n', regModel.coef_)
# The mean squared error
print("Mean squared error: %.2f"
      % mean_squared_error(Y_test, Y_pred))
# Explained variance score: 1 is perfect prediction
print('Variance score: %.2f' % r2_score(Y_test, Y_pred))


