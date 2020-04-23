import math
def performance(labelArr, predictArr):
    #labelArr[i] is actual value,predictArr[i] is predict value
    TP = 0.; TN = 0.; FP = 0.; FN = 0.
    for i in range(len(labelArr)):
        if labelArr[i][0] == 1 and predictArr[i][0] == 1:
            TP += 1.
        if labelArr[i][0] == 1 and predictArr[i][0] == 0:
            FN += 1.
        if labelArr[i][0] == 0 and predictArr[i][0] == 1:
            FP += 1.
        if labelArr[i][0] == 0 and predictArr[i][0] == 0:
            TN += 1.
    SN = TP/(TP + FN) #Sensitivity = TP/P  and P = TP + FN
    SP = TN/(FP + TN) #Specificity = TN/N  and N = TN + FP
    precision=TP/(TP+FP)
    recall=TP/(TP+FN)
    GM=math.sqrt(recall*SP)
    MCC = (TP*TN-FP*FN)/math.sqrt((TP+FP)*(TP+FN)*(TN+FP)*(TN+FN))
    return precision,recall,SN,SP,GM,TP,TN,FP,FN,MCC

import pandas as pd
info_label = pd.read_csv('my_data/PDB14120_cv5_k3.csv',usecols=[0],header=None)
info_predicate = pd.read_csv('my_data/PDB14120_cv5_k3.csv',usecols=[1],header=None)
info_label=info_label.values.tolist()
info_predicate=info_predicate.values.tolist()

precision, recall, SN, SP, GM, TP, TN, FP, FN,MCC = performance(info_label,info_predicate)
print(SN*100.0,SP*100.0,MCC)