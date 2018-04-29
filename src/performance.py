# @performance.py

from AI import *
from calc import *
import csv
result = []
for i in range(35):
    result.append(0)
f = open('output.csv', 'w', encoding='utf-8', newline='')
wr = csv.writer(f)
iteration = 15000
A = AI(123, 987)
A.createList()
answerList = A.answerList

for i in range(iteration):
    '''if i / iteration == 0.9:
        print("\n" * 100)
        print('|=========|')
    elif i / iteration == 0.8:
        print("\n" * 100)
        print('|========-|')
    elif i / iteration == 0.7:
        print("\n" * 100)
        print('|=======--|')
    elif i / iteration == 0.6:
        print("\n" * 100)
        print('|======---|')
    elif i / iteration == 0.5:
        print("\n" * 100)
        print('|=====----|')
    elif i / iteration == 0.4:
        print("\n" * 100)
        print('|====-----|')
    elif i / iteration == 0.3:
        print("\n" * 100)
        print('|===------|')
    elif i / iteration == 0.2:
        print("\n" * 100)
        print('|==-------|')
    elif i / iteration == 0.2:
        print("\n" * 100)
        print('|=--------|')
    elif i / iteration == 0.1:
        print("\n" * 100)
        print('|---------|')'''
    A.answerList = answerList
    A.prediction_list = []
    A.sb_list = []
    answer = 503
    count = 0;
    while(True):
        r = A.model_output()
        count += 1
        if(len(A.answerList) == 1 or check(divide(answer), r) == 30):
            result[count - 1] += 1
            break
        else:
            string = str(check(divide(answer), r))
            if len(string) is 1:
                string = '0' + string
            A.model_input(string[0] + 's' + string[1] + 'b')
            
for i in range(len(result)):
    wr.writerow([i+1, result[i]])
f.close()