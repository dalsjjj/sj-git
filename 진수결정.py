base = int(input("입력 진수 결정(16/10/8/2)"))
number = int(input("값 입력: "), base)
number_16 = hex(number)
number_10 = number
number_8 = oct(number)
number_2 = bin(number)
print(f"16진수 -> {number_16}입니다")
print(f"10진수 -> {number_10}입니다")
print(f"8진수 -> {number_8}입니다")
print(f"2진수 -> {number_2}")