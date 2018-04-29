from random import randrange

def combine(List): #  리스트로 들어온 숫자(예: [1, 2, 3])를 다시 세 자리 숫자(123)로 바꿔줌
    n = len(List)
    result = 0
    for i in range(n):
        result += pow(10, n - i - 1) * List[i]
    return result

def divide(number): # 10 이상의 숫자(예: 123)를 리스트로 바꿔줌([1, 2, 3])
    result = []
    i = 1
    result.append(number % 10)
    while number // (pow(10, i)) != 0:
        result.append(number % pow(10, i + 1) // (pow(10, i)))
        i += 1
    if len(result) == 2:
        result.append(0)
    result.reverse()
    return result

def include_with_certain_digits(answerList, digit, number): # 특정 자릿수에 특정 숫자가 있을 때 include
    result = []
    for i in answerList:
        if(divide(i)[digit] is number):
            result.append(i)
    return result

def include_with_uncertain_digits(answerList, number): # 특정 숫자가 포함될 때 include
    result = []
    for i in answerList:
        try:
            if(divide(i).index(number) >= 0):
                result.append(i)
        except ValueError:
            continue
    return result

def remove_with_uncertain_digits(answerList, number): # 특정 숫자가 포함될 때 remove
    result = []
    for i in answerList:
        try:
            divide(i).index(number)
        except ValueError:
            result.append(i)
            continue
    return result

def parseinput(s): # 사용자가 2s1b 이렇게 입력을 보냈을 때, 문자열을 파싱하는 모듈
    try:
        strike = s[s.index('s') - 1]
    except:
        strike = '0'
    try:
        ball = s[s.index('b') - 1]
    except:
        ball = '0'
    return int(strike + ball)

def return_number_variety(answerList): # 현재 존재하는 정답 리스트의 모든 숫자 variety (얼마나 다양하게 존재하는지) 를 얻는다
    result = set()
    for i in answerList:
        result = result | set(divide(i))
    return result

def return_each_digits_variety(answerList): # 현재 존재하는 정답 리스트에서 각 자릿수의 숫자 variety 를 얻는다
    set0 = set()
    set1 = set()
    set2 = set()
    for i in answerList:
        set0 = set0 | {divide(i)[0]}
        set1 = set1 | {divide(i)[1]}
        set2 = set2 | {divide(i)[2]}
    return [list(set0), list(set1), list(set2)]

def pick_random_number(List): # 리스트 중 랜덤하게 하나를 뽑는다
    return List[randrange(0, len(List))]

def check(number_list, guess):
    strike = 0
    ball = 0
    if(True):
        if ((guess//100) == number_list[0]):
            strike += 1
            guess %= 100
        elif((guess//100) == number_list[1]):
            ball += 1
            guess %= 100
        elif((guess//100) == number_list[2]):
            guess %= 100
            ball += 1
        else:
            guess %= 100
        if ((guess//10) == number_list[1]):
            strike +=1
            guess %= 10
        elif ((guess//10) == number_list[0]):
            ball += 1
            guess %= 10
        elif ((guess//10) == number_list[2]):
            ball += 1
            guess %= 10
        else :
            guess %= 10
        if(guess == number_list[2]):
            strike += 1
        elif(guess == number_list[0]):
            ball += 1
        elif(guess == number_list[1]):
            ball += 1
    return strike * 10 + ball

def detect_ball(List):
    num_list = return_number_variety(List)
    result = []
    for num in num_list:
        should_save = True
        for i in List:
            if not num in divide(i):
                should_save = False
                break
        if should_save:
            result.append(num)
    return result

def detect_strike(List):
    result = [-1, -2, -3]
    var_list = return_each_digits_variety(List)
    for i in range(3):
        if len(var_list[i]) == 1:
            result[i] = var_list[i][0]
    return result