from AI import *
from random import *

strikeball_list = [0, 10, 11, 12, 20]

def find_matches(strikeball, guess, answerList):
    count = 0
    for number in answerList:
        if check(divide(number), guess) == strikeball:
            count += 1
    return count

def get_biggest_matches(guess, answerList):
    result = 0
    global strikeball_list
    for sb in strikeball_list:
        temp = find_matches(sb, guess, answerList)
        if result <= temp:
            result = temp
    return result

def get_biggest_evalutation(answerList):
    if len(answerList) == len(createList()):
        return pick_random_number(answerList), 0
    elif len(answerList) == 1:
        return answerList[0]
    result_guess = 0
    result_eval = 0
    global strikeball_list
    for number in answerList:
        temp = evaluate(get_biggest_matches(number, answerList), len(answerList))
        if result_eval <= temp:
            result_eval = temp
            result_guess = number
    return result_guess, result_eval

def evaluate(x, y):
    # TODO : user defined evaluation function. Default: xy - x^2
    return x * (y - x)

def get_biggest_matches(guess, answerList):
    result = []
    global strikeball_list
    for sb in strikeball_list:
        temp = find_matches(sb, guess, answerList)
        result.append(temp)
    return result

l = createList()[60:600]
t = pick_random_number(l)
print(t, get_biggest_matches(t, l))