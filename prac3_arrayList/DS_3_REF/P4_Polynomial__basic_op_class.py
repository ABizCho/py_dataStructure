# 클래스로 구현.
class Polynomial :
    def __init__( self ):
        self.coef= []

    def degree(self) :
        return len(self.coef) - 1

    def display(self, msg="f(x) = "):
        print("  ", msg, end='')
        deg = self.degree()

        for n in range(deg, 0, -1) :
            print("%5.1f x^%d + " % (self.coef[n], n), end='')
        print("%4.1f"%self.coef[0])

    def add(self, b):
        p = Polynomial()
        if self.degree() > b.degree() :
            p.coef = list(self.coef)
            for i in range(b.degree()+1) :
                p.coef[i] += b.coef[i]
        else :
            p.coef = list(b.coef)
            for i in range(self.degree()+1) :
                p.coef[i] += self.coef[i]
        return p
    
    def subtract(self, b):
        p = Polynomial()
        if self.degree() > b.degree() :
            p.coef = list(self.coef)
            for i in range(b.degree()+1) :
                p.coef[i] -= b.coef[i]
        else :
            p.coef = self.coef
            for i in range(b.degree() - self.degree()):
                self.coef.append(0)
            for i in range(self.degree()+1) :
                p.coef[i] -= b.coef[i]         
        return p
    
    def multiply(self, b):
        P = Polynomial() 
        i=0
        menu = 0
        self_size = len(self.coef)
        b_size = len(b.coef)
        P.items = list(range(self_size + b_size))
        for i in range(len(P.coef)) :
            P.coef[i] = 0 
            
        for i in range(len(self.coef)+1):
            for menu in range(len(b.coef)+1) :
                P.coef[i + menu] = P.coef[i + menu] + self.coef[i]*b.coef[menu]
        return P 
        
        # for menu in range(b_size):
        #     P.coef[i + menu] = P.coef[i + menu ] + self.coef[i]*b.coef[menu]

    def evaluate(self, x):
        result = 0.0
        for i in range(self.degree()+1) :
            result += self.coef[i] * (x**i)
        return result

    # 뺄셈, 곱셈 관련 함수 추가할 것

def read_poly():
    p = Polynomial()
    deg = int(input("다항식의 최고 차수를 입력하시오: "))
    for n in range(deg+1) :
        coef = float(input(  "\tx^%d의 계수 : " % (deg-n)))
        p.coef.append(coef)
    p.coef.reverse()
    return p

# ====================================== 테스트 코드.... 뺄셈, 곱셈 추가할 것
a = read_poly()
b = read_poly()
c = a.add(b)
a.display("A(x) = ")
b.display("B(x) = ")
c.display("C(x) = ")
print("   C(2) = ", c.evaluate(2) )
d = a.subtract(b)
d.display('D(x) = ')

