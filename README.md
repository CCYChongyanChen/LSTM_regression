# LSTM_Linear_regression
a implement of LSTM using Keras for time series prediction regression problem
### Data
the data were from UCI data set. We are using ECG to predict ABP

### Code

1）训练数据需是矩阵型</br>
2）对数据进行规范化，这里用的是最小最大值标准化的规范方法。MinMaxScaler()详情见 https://blog.csdn.net/csmqq/article/details/51461696 </br>
3）拟合输出使用linear，若有正负值可用tanh</br>
4) 训练函数compile中的误差函数选用'mse'</br>

### Denpensies
for the implemention of code, we using Keras to establish LSTM network,  as well as using numpy, pandas, so before you runing this tutorial, it is strongly recommended you install Anaconda which is a package inclueded them all.
### open source protocol
MIT
### contact
author: jinfagang19@163.com
Central South University, Mr. Jin
