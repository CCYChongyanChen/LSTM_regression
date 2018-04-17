# LSTM_Linear_regression
a implement of LSTM using Keras for time series prediction regression problem
### Data
the data were from UCI data set. We are using ECG to predict ABP</br>
To merge all .csv file into one file, strongly recommend the use of .bat or powershell or .cmd</br>
.bat is the fastest, about n sesconds. Powershell will cost about half hour.</br>
### Preprocessing
Using rolling window (min and max)to get the envelope of the PPG\ECG\ABP. Since the data changes a little among long time, using rolling window can give us a overall look. Besides, we need to change ABP into Mean Blood Pressure using transfer learning
### Code
1）Scaler: It is more suitable to use StandardScaler() rather than MinMaxScaler().</br>
2) Loss Function: suggest the loss function to be 'mse'</br>
### Denpensies
for the implemention of code, we using Keras to establish LSTM network,  as well as using numpy, pandas, so before you runing this tutorial, it is strongly recommended you install Anaconda which is a package inclueded them all.
### open source protocol
MIT
### contact
Thanks to the author jinfagang. Based on his work, I apply the code to blood pressure classification and regression.
author: jinfagang19@163.com
Central South University, Mr. Jin

Me: chongyanchen_hci@utexas.edu
