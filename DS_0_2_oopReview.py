'''
객체지향 프로그래밍

    1. 클래스 ( 속성:properties / 메소드 )
    2. 연산자 중복 (operator Overloading)
    3. 상속
'''

'''
< 1. 클래스 >
'''

# class Bike :
#     def __init__(self, name, year, color, speed = 0, isAccident = False) : #생성자 정의 ( 생성자 메소드 정의 내부에 데이터멤버(properties)가 정의된다. )
#         self.name = name    # 데이터 멤버(Property) name 정의 및 초기화
#         self.year = year    # 데이터 멤버(property) year 정의 및 초기화
#         self.color = color  # 데이터 멤버(property) color 정의 및 초기화
#         self.speed = speed  # 데이터 멤버(property) speed 정의 및 초기화
#         self.isAccident = isAccident
        
#     def getProps(self):   # 멤버 함수( method ) 정의
#         print('name: %s\nyear: %d\ncolor: %s\nspeed: %d\nisAccident:%s' %(self.name,self.year,self.color,self.speed,self.isAccident), end='\n')
        
#     def setIsAccident(self):
#         self.isAccident = not(self.isAccident)
    
# Bike1 = Bike('Wolf Classic',2016,'black',120)
# Bike1.getProps()

# Bike1.year = 2015
# Bike1.getProps()

# Bike1.setIsAccident()
# print('\n',Bike1.isAccident)



'''
< 2. 연산자 중복 정의 >
Operator Overloading

    직접 정의한 클래스 객체를 피연산 대상으로 +,-,* 같은 산술 연산자 혹은 비교 연산자 등을 사용하려면,
    객체를 연산 가능한 상태로 만들어야 한다.
    연산자 중복 정의를 통해 클래스 객체를 연산 가능한 상태로 만든다.
    
    연산자 오버로딩? : 클래스 인스턴스 객체끼리 서로 연산을 할 수 있게,
                        기존에 미리 정의돼 있는 내장 연산자의 기능을 바꾸어 중복으로 정의 하는 것.
                        * 산술 연산자 이름 목록 : https://img1.daumcdn.net/thumb/R1280x0/?scode=mtistory2&fname=https%3A%2F%2Fblog.kakaocdn.net%2Fdn%2Fb4xKpO%2FbtqN00MNsNm%2FMBFJNKDsK3z5YoCTSgGegK%2Fimg.png
                        * 비교 연산자 이름 목록 : https://img1.daumcdn.net/thumb/R1280x0/?scode=mtistory2&fname=https%3A%2F%2Fblog.kakaocdn.net%2Fdn%2FcX2qTS%2FbtqN2UFB9NS%2FylKA7cgr1mtyZiLI6NmWE0%2Fimg.png
                        
        -파이썬에서는 '특정 이름'으로 미리 정의된 연산자 메소드를 재정의 하면 연산자 중복정의가 구현된다.
'''

# #     # 연산자 오버로딩이 필요한 이유 예제 : Error Case
# # class NumBox:
# #     def __init__(self,num):
# #         self.num = num
        
# # NumBox1 = NumBox(10)
# # NumBox2 = NumBox(20)

# # NumBox1 + 1 # 에러출력 : 클래스 인스턴스 객체가 연산 가능한 상태가 아니기 때문 : 연산자 오버로딩이 되지 않은 상태
# # print(NumBox1.num)

# # print(NumBox1 + NumBox2) # 에러출력 : 클래스 인스턴스 객체가 연산 가능한 상태가 아니기 때문 : 연산자 오버로딩이 되지 않은 상태



#    # 연산자 오버로딩 예제1 (산술연산자 add)
# class NumBox:
#     def __init__(self,num):
#         self.num = num
        
#     def __add__(self,num):  # add(+) 연산자 오버로딩 : __add__ 는 미리 정의된 수치 연산자
#         self.num += num
    
# NumBox1 = NumBox(10)
# NumBox1 + 1
# print(NumBox1.num)

    
#     # 연산자 오버로딩 예제2 (산술연산자 add)
# class Number:
#     def __init__(self,n):
#         self.n = n
    
#     def __add__(self, other): # add(+) 연산자 오버로딩 : 분기 실행
#         if isinstance(other,Number):
#             return Number(self.n + other.n)
#         elif isinstance(other,int):
#             return Number(self.n + other)
        
# num1 = Number(10)
# num2 = Number(20)

# num1 + 1
# print(num1.n)
# print('\n')

# print(num1 + 1)
# print((num1 + 1).n)
# print('\n')

# print(num1 + num2)
# print((num1 + num2).n)


'''
< 3. 상속 : inheritance >

클래스에서 상속이란, 슈퍼클래스 ( Parent Class, Super Class ) 의 멤버(Props & method)를 서브클래스(Child Class, Sub Class)가 가지게 되는 것이다.

ex) 
부모클래스 : 국가(props:{인구,GDP}, method:{출산율증가(),getGDP()}) 
자식클래스 : 한국,미국,일본,중국 : 국가의 멤버(props,method)를 상속받은 인스턴스 클래스들
'''

# class Country:
#     """Super Class"""

#     name = '국가명'
#     population = '인구'
#     capital = '수도'

#     def show(self):
#         print('국가 클래스의 메소드입니다.')
    
#     def getProps(self):
#         print(self.name)
#         print(self.population)
#         print(self.capital)


# class Korea(Country): # 슈퍼클래스 Country를 상속받은 서브클래스 Korea 정의
#     """Sub Class"""

#     def __init__(self, name):
#         self.name = name

#     def show_name(self):
#         print('국가 이름은 : ', self.name)
        
# class Japan(Country): # 슈퍼클래스 Country를 상속받은 서브클래스 Japan 정의
#     """Sub Class"""
    
#     isSumNara = True
    
#     def __init__(self,name):
#         self.name = name
        
#     def show(self): # 메소드 오버라이딩 : 국가클래스의 메소드 show를 오버라이딩(재정의)
#         print('국가클래스의 show메소드를 오버라이딩한 일본 클래스의 show 메소드입니다.',end="\n")
#         print('섬나라인가? : ',self.isSumNara)
    
#     def getProps(self,isSamurai):
#         super().getProps()
#         print('사무라이?:', isSamurai)
#         print('섬나라?:', self.isSumNara)

# country1 = Country()
# country1.show()
# country1.getProps()

# korea1 = Korea('한국')
# korea1.show()
# korea1.show_name()
# korea1.getProps()

# japan1 = Japan('일본')
# japan1.show()
# japan1.getProps(True)