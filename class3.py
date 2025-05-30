import threading

# 합을 계산하는 함수
def calc_sum(start, end):
    total = 0
    for i in range(start, end + 1):
        total += i
    print(f"{start}+{start+1}+...+{end} = {total}")

# 스레드 객체 생성
t1 = threading.Thread(target=calc_sum, args=(1, 1000))
t2 = threading.Thread(target=calc_sum, args=(1, 100000))
t3 = threading.Thread(target=calc_sum, args=(1, 10000000))

# 스레드 실행
t1.start()
t2.start()
t3.start()
