cross_val_score(estimator , X , Y)
========
X为数据特征 Y为分类(e.g. good or bad)  
1.将一份数据分解为若干个部分，每个部分做以下操作：  
&emsp;&emsp;(1)将X_train，Y_train fit进一个估计器estimator  
&emsp;&emsp;(2)将X和Y根据scoring选取的参数取出一部分作为测试集，剩余部分训练算法  
&emsp;&emsp;(3)对于每个部分测试的结果进行预测准确值的评分，并记录平均得分  

2.最后得出测试数据的命中值集scores,可对其取np.mean(scores)*100观测得分  

Q:  
&emsp;&emsp;cv是对estimator中X_train,Y_train数据进行划分还是对X,Y??

MinMaxScaler().fit_transform(X_broken)
=======
用于将特征值会方法到相同的值域，不会仅仅因为原先特征值的大而具备更强区分度  
&emsp;&emsp;1.将X_broken值域向[0,1]转化,最大为1,最小为0,其余分布在中间  
&emsp;&emsp;2.生成一个新的estomator

Pipeline([(name,processing1),(name2,preprocessing2),....(name_final,'must_be_estimator')])
=====
作为cv的一个参数,对目标数据及进行列表内元组第二个元素的操作，将其名为元组内第一个元素，方便记录数据处理的整个过程并重复     
&emsp;&emsp;1.取出cv中的目标数据集      
&emsp;&emsp;2.对目标数据及进行pipeline内的一系列操作，最后一个元组必须是估计器

LabelEncoder()
================
&emsp;&emsp;用于将fit进容器的数据各自分配一个可数的连续编号,若此时将transform出来的数据用于估计器分类时  
&emsp;&emsp;需考虑特征之间的“距离”,如转化出来的数据为 0 , 1 , 3 , 4 特征之间0,1之间的相似度比0,4之间的相似度高  
&emsp;&emsp;所以当需要做分类操作时,可在此基础上使用one-hot编码  

One-Hot Encoding
==========
例如:  
    自然状态码为：000,001,010,011,100,101  
    独热编码为：000001,000010,000100,001000,010000,100000  
可以这样理解，对于每一个特征，如果它有m个可能值，那么经过独热编后，就变成了m个二元特征（如成绩这个特征有好，中，差变成one-hot就100, 010, 001）。并且，这些特征互斥，每次只有一个激活。因此，数会变成稀疏的。  
```
    enc = preprocessing.OneHotEncoder()
    enc.fit(somedata)
    enc.transform(somedata_needtotrans).toarray()/todense()#化为数组或矩阵
```
举例:

onehot容器fit了一组列表
```
    [[0,0,3],
     [1,1,0],
     [0,2,1],
     [1,0,2]]  
```

可看成是一个矩阵，其每列对应不同的特征取值，每一行对应不同的样本  
- 考虑第一列的取值：  
&emsp;&emsp;有0/1可取，即将0进行编码为 10，将1进行编码为01  
- 考虑第三列的取值：  
&emsp;&emsp;有0/1/2/3可取，即将0，1，2，3分别编码为1000 , 0100 , 0010 , 0001  
将某一组需要转化的数据如[0,1,3]转换后,获得的编码列表为[10, 010, 0001]  
实际输出为[1,0,0,1,0,0,0,0,1]  

np.hstack([a,b,c,d,e...]) np.vstack([a,b,c,d,e,...])
========
    a = [[1,2,3],
         [4,5,6],
         [7,8,9]]

    b = [[a,b,c],
         [d,e,f],
         [g,j,i]]

 np.hstack([a,b])是将a和b按照水平的方式叠在一起(b接在a的后面)
 -------
要求a的行数和b的行数相等，列数可以不相等
    
    则np.hstack([a,b]) =[['1', '2', '3', 'a', 'b', 'c'],
                         ['4', '5', '6', 'd', 'e', 'f'],
                         ['7', '8', '9', 'g', 'j', 'i']]
                         
np.vstack([a,b])是将a和b按照垂直的方式叠在一起(b放在a的下面)
-------

要求a的列数和b的列数相等，行数可以不相等  

    则np.vstack([a,b]) =[['1', '2', '3'],
                         ['4', '5', '6'],
                         ['7', '8', '9'],
                         ['a', 'b', 'c'],
                         ['d', 'e', 'f'],
                         ['g', 'j', 'i']]

GridSearchCV(estimator , paramter_space)
=========
    parameter = {
    "max_features" : [2,10, 'auto'],
    "n_estimators" : [100,],
    "criterion" : ["gini" , 'entropy'],
    "min_samples_leaf" : [2,4,6],}

设置parameter_space,GridSearchCV会遍历所有情况，找到一个最好的参数集(最佳参数)  
+ GridSearchCV(estimator , paramter_space).fit(X , Y)
+ GridSearchCV(estimator , paramter_space).best_score_#输出最佳准确值
+ GridSearchCV(estimator , paramter_space).best_estmator_#输出正确率最高的模型所用到的参数