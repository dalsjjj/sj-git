inFp = None
inStr = ""

inFp = open("C:\\Users\\mmssj\\OneDrive\\바탕 화면\\code\\sj-git\\filetest\\data1.txt", "r", encoding="UTF8")

inList = inFp.readlines()

for i, line in enumerate(inList, start=1):
    print(f"{i}. {line.strip()}")

inFp.close()