select = int(input("1. 입력한 수식 계산 2. 두 수 사이의 합계 :"))

if select == 1:
    a = input(" *** 수식을 입력하세요: ")
    b = eval(a)
    print(" %s 결과는 %5.1f 입니다. " %(a,b))

elif select == 2 :
    c = int(input("*** 첫 번째 숫자를 입력하세요 : "))
    d = int(input(" *** 두 번째 숫자를 입력하세요 : "))
    e = int((c + d) * (d - c + 1) * 1/2)
    print(c,"+...+", d ,"는", e, "입니다")
else : 
    print("1이나 2만 입력하세요")


    