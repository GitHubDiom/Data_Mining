# Data_Mining

## cross_val_score(estimator , X , Y)
	X为数据特征 Y为分类(e.g. good or bad)
    1.将一份数据分解为若干个部分，每个部分做以下操作
        (1)将X_train，Y_train fit进一个估计器estimator
        (2)将X和Y根据scoring选取的参数取出一部分作为测试集，剩余部分训练算法
        (3)对于每个部分测试的结果进行预测准确值的评分，并记录平均得分
    2.最后得出测试数据的命中值集scores,可对其取np.mean(scores)*100观测 
    question:
        cv是对estimator中X_train,Y_train数据进行划分还是对X,Y??
## MinMaxScaler().fit_transform(X_broken)
    用于将特征值会方法到相同的值域，不会仅仅因为原先特征值的大而具备更强区分度
    1.将X_broken值域向[0,1]转化,最大为1,最小为0,其余分布在中间
    2.生成一个新的集合用于放入cv

## Pipeline([(name,processing1),(name2,preprocessing2),....(name_final,'must_be_estimator')])
    作为cv的一个参数,对目标数据及进行列表内元组第二个元素的操作，将其命名为元组内第一个元素
    方便记录数据处理的整个过程
    1.取出cv中的目标数据集
    2.对目标数据及进行pipeline内的一系列操作，最后一个元组必须是估计器
    
<<<<<<< HEAD
## 
=======
>>>>>>> 9373ac84197e4210aaa75d1829b963196eec4306
