
from django.shortcuts import render

from django.http import HttpResponse
# Create your views here.
def calculator(request):
    #return HttpResponse('계산기 기능 구현 시작입니다')

    #1. 데이터 확인
    num1 = (request.GET.get('num1'))
    num2 = (request.GET.get('num2'))
    operators = request.GET.get('operators')

    #2. 계산
    if operators == '+':
        result = int(num1) + int(num2)
    elif operators =='-':
        result = int(num1) - int(num2)
    elif operators == '/':
        result = int(num1) / int(num2)
    elif operators == '*':
        result = int(num1) * int(num2)
    else:
        result = 0

    #3. 응답
    return render(request, 'calculator.html', {'result': result})


def lotto(request):
    import random  # import 파일 최상단에 위치하는게 윈칙
    pull_number = None
    lotto_number = None

    pull_number 
    lotto_number = list()
    for _ in range(7):
        number = random.randint(1, 45)
        lotto_number.append(number)

    return render(request, 'lotto.html',{'lotto_number': lotto_number})