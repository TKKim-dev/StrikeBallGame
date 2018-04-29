from calc import *
from random import *

class AI:
    prediction_list = []
    sb_list = []
    x_list = []
    answerList = []
    number_scope = None
    most_recent_guess = None


    def __init__(self, starts_with, ends_with):
        self.number_scope = (starts_with, ends_with)
        self.createList()
        
        
    def createList(self):
        temp = self.number_scope[0]
        while(temp <= self.number_scope[1]):
            has_same_number = False
            digits = divide(temp)
            n = len(digits)
            for i in range(n-1):
                for j in range(n-1-i):
                    if digits[i] is digits[i+j+1]:
                        has_same_number = True
            if not has_same_number:
                self.answerList.append(temp)
            temp += 1


    def model_input(self, response):
        answerList = self.answerList
        response = parseinput(response)
        self.sb_list.append(response)
        guess = divide(self.most_recent_guess)
        if len(guess) is 2:
            guess.insert(0, 0)
        if(response is 30): # 3스트라이크
            answerList = combine([guess[0], guess[1], guess[2]])
        elif(response is 0): # 3아웃
            for i in range(3):
               answerList = remove_with_uncertain_digits(answerList, guess[i])
        elif(response is 1): # 1볼
            temp = dict()
            A = set(include_with_uncertain_digits(answerList, guess[0])) - set(include_with_certain_digits(answerList, 0, guess[0]))
            B = set(include_with_uncertain_digits(answerList, guess[1])) - set(include_with_certain_digits(answerList, 1, guess[1]))
            C = set(include_with_uncertain_digits(answerList, guess[2])) - set(include_with_certain_digits(answerList, 2, guess[2]))
            answerList = list(A | B | C)
        elif(response is 2): # 2볼
            A = (set(include_with_uncertain_digits(answerList, guess[0])) & set(include_with_uncertain_digits(answerList, guess[1]))) - (set(include_with_certain_digits(answerList, 0, guess[0])) & set(include_with_certain_digits(answerList, 1, guess[1])))
            B = (set(include_with_uncertain_digits(answerList, guess[1])) & set(include_with_uncertain_digits(answerList, guess[2]))) - (set(include_with_certain_digits(answerList, 1, guess[1])) & set(include_with_certain_digits(answerList, 2, guess[2])))
            C = (set(include_with_uncertain_digits(answerList, guess[2])) & set(include_with_uncertain_digits(answerList, guess[0]))) - (set(include_with_certain_digits(answerList, 2, guess[2])) & set(include_with_certain_digits(answerList, 0, guess[0])))
            answerList = list(A | B | C)
        elif(response is 10): # 1스트라이크
            A = set(include_with_certain_digits(answerList, 0, guess[0]))
            B = set(include_with_certain_digits(answerList, 1, guess[1]))
            C = set(include_with_certain_digits(answerList, 2, guess[2]))
            answerList = list(A | B | C)
        elif(response is 11): # 1스트라이크 1볼
            A = (set(include_with_certain_digits(answerList, 0, guess[0])) & set(include_with_certain_digits(answerList, 1, guess[2]))) | (set(include_with_certain_digits(answerList, 0, guess[0])) & set(include_with_certain_digits(answerList, 2, guess[1])))
            B = (set(include_with_certain_digits(answerList, 1, guess[1])) & set(include_with_certain_digits(answerList, 0, guess[2]))) | (set(include_with_certain_digits(answerList, 1, guess[1])) & set(include_with_certain_digits(answerList, 2, guess[0])))
            C = (set(include_with_certain_digits(answerList, 2, guess[2])) & set(include_with_certain_digits(answerList, 0, guess[1]))) | (set(include_with_certain_digits(answerList, 2, guess[2])) & set(include_with_certain_digits(answerList, 1, guess[0])))
            answerList = list(A | B | C)
        elif(response is 12): # 1스트라이크 2볼
            A = (set(include_with_certain_digits(answerList, 0, guess[0])) & set(include_with_certain_digits(answerList, 1, guess[2])) & set(include_with_certain_digits(answerList, 2, guess[1])))
            B = (set(include_with_certain_digits(answerList, 1, guess[1])) & set(include_with_certain_digits(answerList, 0, guess[2])) & set(include_with_certain_digits(answerList, 2, guess[0])))
            C = (set(include_with_certain_digits(answerList, 2, guess[2])) & set(include_with_certain_digits(answerList, 0, guess[1])) & set(include_with_certain_digits(answerList, 1, guess[0])))
            answerList = list(A | B | C)
        elif(response is 20): # 2스트라이크
            A = (set(include_with_certain_digits(answerList, 0, guess[0])) & set(include_with_certain_digits(answerList, 1, guess[1])))
            B = (set(include_with_certain_digits(answerList, 1, guess[1])) & set(include_with_certain_digits(answerList, 2, guess[2])))
            C = (set(include_with_certain_digits(answerList, 2, guess[2])) & set(include_with_certain_digits(answerList, 0, guess[0])))
            answerList = list(A | B | C)
        answerList = list(set(answerList) - {100 * guess[0] + 10 * guess[1] + guess[2]}) # 사용자의 guess 를 정답 리스트에서 제거
        self.answerList = answerList
        self.consider_past_predictions()
    
    
    def model_output(self):
        answerList = self.answerList
        if(len(answerList) is 0):
            return -1
        elif(len(answerList) is 1):
            self.add_to_prediction(answerList[0])
            return answerList[0]
        elif(len(answerList) is 2):
            result = pick_random_number(answerList)
            self.add_to_prediction(result)
            return result
        result = []
        variety_lists = return_each_digits_variety(answerList)
        digit_list = []
        for i in range(3):
            if(len(variety_lists[i]) is 1):
                digit_list.append(i)
        if(len(digit_list) is 0):
            temp = pick_random_number(answerList)
            self.add_to_prediction(temp)
            return temp
        elif(len(digit_list) is 1):
            result = divide(pick_random_number(answerList))
            total_set = set()
            for l in variety_lists:
                total_set = total_set | (set(l))
            if(len(total_set - set(result)) != 0):
                total_set = total_set - set(result)
            result[digit_list[0]] = pick_random_number(list(total_set)) # 나머지 두 자리 중에 랜덤하게 골라서, 거기서 pick 되지 않은 숫자를 고른다.
            temp = combine(result)
            self.add_to_prediction(temp)
            return temp
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
            temp = combine(result)
            self.add_to_prediction(temp)
            return temp
        
    def check_valid(self, answer):
        p_list = self.prediction_list
        sb_list = self.sb_list
        print(p_list)
        for i in range(len(p_list)):
            print('AI는', i + 1, '회에', p_list[i], '라고 물었고,',
			'당신은', str(int(sb_list[i] / 10)) + 's' + str(int(sb_list[i] % 10)) + 'b 라고 답했습니다. ',
			'<Enter>')
            input()
            temp = check(divide(p_list[i]), answer)
            if(sb_list[i] is temp):
                print('맞게 입력하셨네요 :) ', i + 2, '회를 확인해보겠습니다. <Enter>')
                input()
            else:
                print('여기서 헷갈리셨네요. ' + str(int(sb_list[i] / 10)) + 's' + \
                      str(int(sb_list[i] % 10)) + 'b가 아닌',
                      str(int(temp / 10)) + 's' + \
                      str(int(temp % 10)) + 'b가 맞습니다 :( ',
                      '<Enter>')
                input()
                if(i is len(p_list) -1):
                    print('----------------------\n그리고', i + 1 ,'회에서 게임이 끝났습니다. \n\n누구나 헷갈릴 수 있어요 :) \n다음에 또 도전해주세요!')
                    input()
    
    def consider_past_predictions(self):
        #ball = detect_ball(self.answerList)
        strike = detect_strike(self.answerList)
        if strike == [-1,-2,-3]:
            return
        for i in range(len(self.prediction_list)):
            if self.sb_list[i] - check(strike, self.prediction_list[i]) <= 0:
                for j in range(3):
                    try:
                        index = strike.index(i - 3)
                        self.x_list.append(divide(self.prediction_list[i])[index])
                    except ValueError:
                        continue
        for i in self.x_list:
            remove_with_uncertain_digits(self.answerList, i)
        self.x_list = []
    def print_answerList(self):
        print(len(self.answerList))
        print(sorted(self.answerList))
    def add_to_prediction(self, number):
        self.prediction_list.append(number)
        self.most_recent_guess = number
#-----------------------------------------------------------------------------#
    #def searchfor_strikeball(self):
