# @performance.py

from AI import *
import csv

f = open('output.csv', 'w', encoding='utf-8', newline='')
wr = csv.writer(f)
iteration = 15000

for i in range(iteration):
    List = createList()
    random = pick_random_number(List)
    count = 0;
    while(True):
        r = model_output(List)
        count += 1
        if(len(List) == 1 or check(divide(random), r) == 30):
            List = [r]
            print(i ,'번째: ', count, '회 만에 성공')
            wr.writerow([count])
            break
        else:
            List = model_input(List, divide(r), check(divide(random), r))
f.close()