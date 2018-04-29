from AI import *
from random import *

input("123 ~ 987 까지, 중복 없이 숫자를 하나 생각해주세요. (Enter)")
input("AI의 추측에 대해 스트라이크와 볼의 여부를 다음과 같은 4자리 형식으로 알려주세요. \n(Ex. 1s1b, 0s2b, 3s0b, 0 등) (Enter)")
YorN = input("정말 세자리 숫자를 생각하셨나요~? (Y / N)")
while(YorN.upper() != 'Y'):
    YorN = input('준비되면 Y를 입력해주세요 (Y / N)')

A = AI(123, 987)
count = 0
while(True):
    count += 1
    prediction = A.model_output()
    if(prediction is -1):
        answer = input('이런, AI가 답을 모르겠다고 합니다 :( 원래 무슨 숫자를 생각하셨는지 알려주세요 : ')
        A.check_valid(int(answer))
        break
    print("\nAI 의 추측은", prediction, "입니다. 스트라이크와 볼 여부를 입력해주세요 : ")
    result = input()
    if(result == '3s'):
        print("AI 가", count, "회에 정답을 맞추었습니다.")
        input()
        break
    else:
        l = A.model_input(result)
        A.print_answerList()
        temp = detect_ball(A.answerList)
        if temp != []:
            print('ball:',temp)
        temp = detect_strike(A.answerList)
        if temp != [-1,-2,-3]:
            print('strike:',temp)