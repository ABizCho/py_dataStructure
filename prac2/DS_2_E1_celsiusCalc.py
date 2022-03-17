def celsiusCalc() :
    cel = float(input('섭씨 온도를 입력하세요(ºC) :'))
    fah = 32 + 180/100*cel
    
    print(fah,'ºF')
    return fah

celsiusCalc()