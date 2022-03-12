# def recursive(n) :  // 종료조건이 없으므로 에러출력
#   if n == 1:
#     return 0
#   print(n)
#   return n * recursive(n)

# recursive(3)

# def hello(count) :
#   if count == 0 :
#     return

#   print('Hello, world!',count)

#   count -= 1
#   hello(count)

# hello(5)

# # 1.11 다음과 같은 순환적인 프로그램에서 sub(3) 과 같이 호출할때 함수 sub()가 호출되는 횟수는?
# def sub(n):
#   print('실행됨')
#   if n <= 1 :
#     return n
#   return sub(n-1) + sub(n-2)

# sub(3)


# # 1.13 다음 함수를 sum(5)로 호출하였을 때, 화면에 출력되는 내용과 함수의 반환값을 구하시오.

# def sum(n):
#       print(n)
#       if n<1:
#             return 0;
#       else:
#             return n + sum(n-1)

# a = sum(5)
# print('반환값 : ',a)


# 1.14 다음 함수에서 asterisk(5)와 같이 호출 할 때 출력되는 *의 개수는?
def asterisk(i):
  if i > 1 :
    asterisk( i / 2 )
    asterisk( i / 2 )
  print('*',end='')

asterisk(5)