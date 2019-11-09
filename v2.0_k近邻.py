import numpy as np
import operator

def creatData():
    group = np.array([[2,3],[5,4],[9,6],[4,7],[8,1],[7,2]])
    lables = ['A','B','D','C','A','C',]
    return group,lables

def classify(inX, dataSet, lables, k):
    dataSetSize = dataSet.shape[0]
    print(dataSetSize)
    difMat = np.tile(inX, (dataSetSize,1)) - dataSet
    print(difMat)
    difMat = difMat**2
    print(difMat)
    difMat = difMat.sum(axis=1)
    print(difMat)
    sortDis = difMat.argsort()
    print(sortDis)

    classcount = {}

    for i in range(k):
        voteLable = lables[sortDis[i]]
        classcount[voteLable] = classcount.get(voteLable,0) +1

    print(classcount)

    maxCount = 0
    for key,value in classcount.items():
        if value > maxCount:
            maxCount = value
            classes = key

    return classes

dataSet, lables = creatData()
classes = classify([0,0], dataSet, lables, 4)

print("类别为{0}".format(classes))

