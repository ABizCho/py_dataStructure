'''
UP DOWN GAME
'''

import random

def UPDOWN() :
    num = random.randint(0, 100)
    tries = 0
    Try = 0
    MinHint = 0
    MaxHint = 99
    
    for n in range(10) :
        Try = int(input('( %d ~ %d ) 의 숫자를 입력하세요: '%(MinHint, MaxHint)))
        tries += 1
        
        if num == Try:
            print('정답입니다. %d회 만에 맞췄습니다.'%(n+1))
            break
        elif num < Try:
            print('Down')
            MaxHint = Try
        elif num > Try :
            print('Up')
            MinHint = Try
    if tries > n:
        print('10회 시도를 실패하였습니다, 종료합니다.')
        
UPDOWN()
    
    
