inFp, outFp = None, None
inStr = ""

# 소스 및 타깃 파일명을 입력받음
inFilename = input("소스 파일명을 입력하세요 : ")
outFilename = input("타깃 파일명을 입력하세요 : ")

# 파일 열기
inFp = open(inFilename, "r")
outFp = open(outFilename, "w")

# 파일 내용 복사
inList = inFp.readlines()
for inStr in inList:
    outFp.writelines(inStr)

# 파일 닫기
inFp.close()
outFp.close()

print(f"--- {inFilename} 파일이 {outFilename} 파일로 복사되었음 ---")