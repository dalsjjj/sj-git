inFp = None
inList, inStr = [], ""

inFp = open("C:\\Users\\mmssj\\OneDrive\\바탕 화면\\code\\sj-git\\filetest\\data1.txt", "r", encoding="UTF8")
inList = inFp.readlines()

for i, inStr in enumerate(inList):
    print(f"{i + 1}: {inStr}", end="")

inFp.close()