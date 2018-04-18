from AI import *
from random import *

input("123 ~ 987 까지, 중복 없이 숫자를 하나 생각해주세요. (Enter)")
input("AI의 추측에 대해 스트라이크와 볼의 여부를 다음과 같은 4자리 형식으로 알려주세요. \n(Ex. 1s1b, 0s2b, 3s0b, 0 등) (Enter)")
YorN = input("정말 세자리 숫자를 생각하셨나요~? (Y / N)")
while(YorN.upper() != 'Y'):
    YorN = input('준비되면 Y를 입력해주세요 (Y / N)')

l = createList()
prediction_list = [] #AI의 추측을 저장
sb_list = [] #스트라이크와 볼 여부를 저장
count = 0
while(True):
    count += 1
    temp = get_evaluation(l)
    prediction = max(temp, key = temp.get)
    if(prediction is -1):
        answer = input('이런, AI가 답을 모르겠다고 합니다 :( 원래 무슨 숫자를 생각하셨는지 알려주세요 : ')
        check_valid(prediction_list, sb_list, int(answer))
        input()
        break
    print("\nAI 의 추측은", prediction, "입니다. 스트라이크와 볼 여부를 입력해주세요 : ")
    if(count is not 1):
        print(temp)
    result = input()
    prediction_list.append(prediction)
    sb_list.append(parseInput(result))
    if(result == '3s'):
        print("AI 가", count, "회에 정답을 맞추었습니다.")
        input()
        break
    else:
        l = model_input(l, divide(prediction), parseInput(result))
