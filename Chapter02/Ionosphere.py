import os,csv 
import numpy as np
from sklearn.cross_validation import train_test_split,cross_val_score
from sklearn.neighbors import KNeighborsClassifier
from matplotlib import pyplot as plt
from sklearn.preprocessing import MinMaxScaler
from sklearn.pipeline import Pipeline
X = np.zeros((351,34) , dtype='float')
Y = np.zeros((351,) , dtype='bool')
def loop():
    for N_neighbors in parameter_value:
        estimator = KNeighborsClassifier(n_neighbors=N_neighbors)#default n_neighbors = 5
        estimator.fit(X_train , Y_train)
        #Y_predicted = estimator.predict(X_test)#直接进行估计  此步骤为可选步骤1
        #accuracy = np.mean(Y_predicted == Y_test)
        #print('{:.1f}%'.format(accuracy*100))
        '''  cross_val_score
        X为数据特征 Y为分类结果(g or b)
        1.将一份数据分解为若干个部分，每个部分做以下操作
            (1)将X和Y根据scoring选取的参数取出一部分作为测试集，剩余部分训练算法
            (2)对于每个部分测试的结果进行预测准确值的评分，并记录平均得分
        2.最后得出测试数据的准确值  '''
        score = cross_val_score(estimator , X , Y, scoring = 'accuracy')#通过交叉检验进行估计 可选步骤2
        all_score.append(score)
        
        avg_score.append(np.mean(score))
        print("broken:{0:.1f}%".format(np.mean(score*100)))
        X_transformed = MinMaxScaler().fit_transform(X_broken)
        estimator = KNeighborsClassifier(n_neighbors=N_neighbors)
        broken_score = cross_val_score(estimator , X_transformed, Y ,scoring = 'accuracy')
        print('fixed:',np.mean(broken_score)*100)

data_filename = './ionosphere.data'
with open(data_filename,'r') as f:
    reader = csv.reader(f)
    for i , row in enumerate(reader):
        data = [float(each_data) for each_data in row[:-1]]
        X[i] = data
        Y[i] = row[-1]=='g'

X_train , X_test , Y_train , Y_test = train_test_split(X, Y ,random_state = 14)
parameter_value = list(range(1,21))
avg_score = []
all_score = []
'''     1.对X集合进行一定程度的破坏，使其极差增大，影响预测值
        2.对X_broken中的值进行规范化至[0,1]，预测值恢复 '''
X_broken = np.array(X)
X_broken[:,::2]/=10
#loop()
scaling_pipeline = Pipeline([('normalizate',MinMaxScaler()),('predict',KNeighborsClassifier())])
#X_transformed = MinMaxScaler().fit_transform(X_broken)
#estimator = KNeighborsClassifier()
'''     将X_broken输入scaling_pipeline进行操作，最后一步输入估计器  '''
broken_score = cross_val_score(scaling_pipeline , X_broken, Y ,scoring = 'accuracy')
print('fixed:',np.mean(broken_score)*100)

#print("{:.1f}%".format(np.array(avg_score,dtype='float').mean()*100))
#plt.plot(parameter_value,avg_score)



