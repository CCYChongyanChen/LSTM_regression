# LSTM_Linear_regression
a implement of LSTM using Keras for time series prediction regression problem
### Data
the data were from UCI data set. We are using ECG to predict ABP</br>
To merge all .csv file into one file, strongly recommend the use of .bat or powershell or .cmd</br>
.bat is the fastest, about n sesconds. Powershell will cost about half hour.</br>

### Code

1）训练数据需是矩阵型</br>
2）对数据进行规范化，这里试用了最小最大值标准化的规范方法MinMaxScaler()和StandardScaler()方法, StandardScaler效果较好，因为数据并不集中在0附近</br>
详情见 https://blog.csdn.net/csmqq/article/details/51461696 </br>
minmaxscaler()</br>
![image](https://github.com/ccy961226/LSTM_regression/edit/master/png/MinMaxscaler.png)</br>
standardscaler</br>
![image](https://github.com/ccy961226/LSTM_regression/edit/master/png/standardscaler.png)</br>
3）拟合输出使用linear，若有正负值可用tanh</br>
4) 训练函数compile中的误差函数选用'mse'</br>

### Denpensies
for the implemention of code, we using Keras to establish LSTM network,  as well as using numpy, pandas, so before you runing this tutorial, it is strongly recommended you install Anaconda which is a package inclueded them all.
### open source protocol
MIT
### contact
author: jinfagang19@163.com
Central South University, Mr. Jin
