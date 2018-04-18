from random import *

strikeball_list = [0, 10, 11, 12, 20]

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

def combine(a): #  리스트로 들어온 숫자(예: [1, 2, 3])를 다시 세 자리 숫자(123)로 바꿔줌
    return 100 * a[0] + 10 * a[1] + a[2]

def createList(): # 가능한 정답 집합을 초기화(생성)한다. 123~987 까지의 9*9*8 개의 숫자들
    List = []
    temp = 123
    while(temp <= 987):
        digits = divide(temp)
        if(digits[0] is not digits[1] and digits[1] is not digits[2] and digits[2] is not digits[0]):
            List.append(temp)
        temp += 1
    return List

def divide(a): # 3자리 숫자(예: 123)를 리스트로 바꿔줌([1, 2, 3])
    x = a // 100
    a %= 100
    y = a // 10
    a %= 10
    z = a
    result = [x, y, z]
    return result

def parseInput(s): # 사용자가 2s1b 이렇게 입력을 보냈을 때, 문자열을 파싱하는 모듈
    try:
        strike = s[s.index('s') - 1]
    except:
        strike = '0'
    try:
        ball = s[s.index('b') - 1]
    except:
        ball = '0'
    return int(strike + ball)

def pick_random_number(answerList): # 현재의 정답 리스트 중 랜덤하게 하나를 뽑는다
    return answerList[randrange(0, len(answerList))]

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


# 사용자가 입력한 답변이 맞는지 하나하나 확인하는 메서드
# r_list 는 AI 쪽 추측, sb_list 는 사용자 쪽 답변(0s0b 형식), answer는 최종 정답
def check_valid(r_list, sb_list, answer):
    for i in range(len(r_list)):
        print('AI는', i + 1, '회에', r_list[i], '라고 물었고,', '당신은', str(int(sb_list[i] / 10)) + 's' + str(int(sb_list[i] % 10)) + 'b 라고 답했습니다.  <Enter>')
        input()
        temp = check(divide(r_list[i]), answer)
        if(sb_list[i] is temp):
            print('맞게 입력하셨네요 :) ', i + 2, '회를 확인해보겠습니다. <Enter>')
            input()
        else:
            print('여기서 헷갈리셨네요. ' + str(int(sb_list[i] / 10)) + 's' + str(int(sb_list[i] % 10)) + 'b가 아닌', str(int(temp / 10)) + 's' + str(int(temp % 10)) + 'b가 맞습니다 :(  <Enter>')
            input()
            if(i is len(r_list) -1):
                print('----------------------\n그리고', i + 1 ,'회에서 게임이 끝났습니다. \n\n누구나 헷갈릴 수 있어요 :) \n다음에 또 도전해주세요!')
				
def model_input(answerList, guess, result):
    if(result is 30): # 3스트라이크
        answerList = [guess[0] * 100 + guess[1] * 10 + guess[2]]
        return answerList
    elif(result is 0): # 3아웃
        for i in range(3):
           answerList = remove_with_uncertain_digits(answerList, guess[i])
    elif(result is 1): # 1볼
        A = set(include_with_uncertain_digits(answerList, guess[0])) - set(include_with_certain_digits(answerList, 0, guess[0]))
        B = set(include_with_uncertain_digits(answerList, guess[1])) - set(include_with_certain_digits(answerList, 1, guess[1]))
        C = set(include_with_uncertain_digits(answerList, guess[2])) - set(include_with_certain_digits(answerList, 2, guess[2]))
        answerList = list(A | B | C)
    elif(result is 2): # 2볼
        A = (set(include_with_uncertain_digits(answerList, guess[0])) & set(include_with_uncertain_digits(answerList, guess[1]))) - (set(include_with_certain_digits(answerList, 0, guess[0])) & set(include_with_certain_digits(answerList, 1, guess[1])))
        B = (set(include_with_uncertain_digits(answerList, guess[1])) & set(include_with_uncertain_digits(answerList, guess[2]))) - (set(include_with_certain_digits(answerList, 1, guess[1])) & set(include_with_certain_digits(answerList, 2, guess[2])))
        C = (set(include_with_uncertain_digits(answerList, guess[2])) & set(include_with_uncertain_digits(answerList, guess[0]))) - (set(include_with_certain_digits(answerList, 2, guess[2])) & set(include_with_certain_digits(answerList, 0, guess[0])))
        answerList = list(A | B | C)
    elif(result is 10): # 1스트라이크
        A = set(include_with_certain_digits(answerList, 0, guess[0]))
        B = set(include_with_certain_digits(answerList, 1, guess[1]))
        C = set(include_with_certain_digits(answerList, 2, guess[2]))
        answerList = list(A | B | C)
    elif(result is 11): # 1스트라이크 1볼
        A = (set(include_with_certain_digits(answerList, 0, guess[0])) & set(include_with_certain_digits(answerList, 1, guess[2]))) | (set(include_with_certain_digits(answerList, 0, guess[0])) & set(include_with_certain_digits(answerList, 2, guess[1])))
        B = (set(include_with_certain_digits(answerList, 1, guess[1])) & set(include_with_certain_digits(answerList, 0, guess[2]))) | (set(include_with_certain_digits(answerList, 1, guess[1])) & set(include_with_certain_digits(answerList, 2, guess[0])))
        C = (set(include_with_certain_digits(answerList, 2, guess[2])) & set(include_with_certain_digits(answerList, 0, guess[1]))) | (set(include_with_certain_digits(answerList, 2, guess[2])) & set(include_with_certain_digits(answerList, 1, guess[0])))
        answerList = list(A | B | C)
    elif(result is 12): # 1스트라이크 2볼
        A = (set(include_with_certain_digits(answerList, 0, guess[0])) & set(include_with_certain_digits(answerList, 1, guess[2])) & set(include_with_certain_digits(answerList, 2, guess[1])))
        B = (set(include_with_certain_digits(answerList, 1, guess[1])) & set(include_with_certain_digits(answerList, 0, guess[2])) & set(include_with_certain_digits(answerList, 2, guess[0])))
        C = (set(include_with_certain_digits(answerList, 2, guess[2])) & set(include_with_certain_digits(answerList, 0, guess[1])) & set(include_with_certain_digits(answerList, 1, guess[0])))
        answerList = list(A | B | C)
    elif(result is 20): # 2스트라이크
        A = (set(include_with_certain_digits(answerList, 0, guess[0])) & set(include_with_certain_digits(answerList, 1, guess[1])))
        B = (set(include_with_certain_digits(answerList, 1, guess[1])) & set(include_with_certain_digits(answerList, 2, guess[2])))
        C = (set(include_with_certain_digits(answerList, 2, guess[2])) & set(include_with_certain_digits(answerList, 0, guess[0])))
        answerList = list(A | B | C)
    answerList = list(set(answerList) - {100 * guess[0] + 10 * guess[1] + guess[2]}) # 사용자의 guess 를 정답 리스트에서 제거
    return answerList


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
	
def model_output(answerList):
    if(len(answerList) is 0):
        return -1
    elif(len(answerList) is 1):
        return answerList[0]
    result = []
    variety_lists = return_each_digits_variety(answerList)
    digit_list = []
    for i in range(3):
        if(len(variety_lists[i]) is 1):
            digit_list.append(i)
    if(len(digit_list) is 0):
        return pick_random_number(answerList)
    elif(len(digit_list) is 1):
        result = divide(pick_random_number(answerList))
        total_set = set()
        for l in variety_lists:
            total_set = total_set | (set(l))
        if(len(total_set - set(result)) != 0):
            total_set = total_set - set(result)
        result[digit_list[0]] = pick_random_number(list(total_set)) # 나머지 두 자리 중에 랜덤하게 골라서, 거기서 pick 되지 않은 숫자를 고른다.
        return combine(result)
    elif(len(digit_list) is 2):
        result = divide(pick_random_number(answerList))
        total_set = set()
        for l in variety_lists:
            total_set = total_set | (set(l))
        total_set = total_set - set(result)
        for i in range(2):
            if(len(total_set) is 0):
                break
            result[digit_list[i]] = pick_random_number(list(total_set))
            total_set = total_set - set(result)
        return combine(result)

#------------------------------------------------------------------------------#

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

def get_evaluation(answerList):
    result_dict = dict()
    if(len(answerList) is 0):
        return {-1:0}
    elif len(answerList) == 1:
        return {answerList[0]:0}
    elif len(answerList) == len(createList()):
        return {pick_random_number(answerList): 0}
    biggest_ev = 0
    global strikeball_list
    for number in answerList:
        temp = evaluate(get_biggest_matches(number, answerList), len(answerList))
        result_dict[number] = temp
        if biggest_ev <= temp:
            biggest_ev = temp
    return result_dict

def evaluate(x, y):
    # TODO : user defined evaluation function. Default: xy - x^2
    return x * (y - x)