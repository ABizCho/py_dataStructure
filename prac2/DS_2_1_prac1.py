'''
세후임금 계산기
'''
# def TaxCalc() :
#     income = int(input('Enter your income: '))
    
#     if income <= 1200 :
#         Tax = income*0.06
#         if income <= 4600 :
#             Tax = Tax + (income-1200)*0.15
#             if income <= 8800 :
#                 Tax = Tax + (income-4600)*0.24
#                 if income <= 15000 :
#                     Tax = Tax + (income-8800)*0.35
#                     if income > 15000 :
#                         Tax = Tax + (income-15000)*0.38
                        
#     afterIncome = income
#     print('Tax: ',Tax ,', ','After Income: ',afterIncome)
    
# TaxCalc()


'''
정답코드
'''
income = int(input("연봉을 입력하세요 ==> "))

total = income
tax = 0

if income > 15000:
 	tax += (income - 15000)*0.38
 	income = 15000
if income > 8800:
 	tax += (income - 8800)*0.35
 	income = 8800
if income > 4600 :
 	tax += (income - 4600)*0.24
 	income = 4600
if (income > 1200):
 	tax += (income - 1200)*0.15
 	income = 1200

tax += income*0.06
print(" 전체세금 = ", tax)
print(" 순수소득 = ", total - tax)