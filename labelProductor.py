def labelProduct(numberOf1,numberOf0):
    fi = open('./train_label03.txt','a+')
    for i in range(numberOf1):
        fi.write('1'+'\n')
    for i in range(numberOf0):
        fi.write('0'+'\n')
    fi.close

labelProduct(5838,6889)