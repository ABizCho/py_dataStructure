# UP DOWN GAME

import random

def UPDOWN() :
    num = random.randint(0, 100)
    tries = 0
    Try = 0
    MaxHint = 100
    MinHint = 0
    
    for i in range(1,11) :
        Try = int(input('( %d ~ %d ) 의 숫자를 입력하세요: '%(MinHint, MaxHint)))
        tries += 1
        
        if num == Try:
            print('정답입니다')
            break
        elif num < Try:
            print('Down')
            MaxHint = Try
        elif num > Try :
            print('Up')
            MinHint = Try
    if tries > i:
        print('10회 시도를 실패하였습니다, 종료합니다.')
        
UPDOWN()
    
    
