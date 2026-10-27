with open("C:/Users/STUDENT/Downloads/aw_pilseta.csv", "r", encoding="utf-8") as file:
    text = file.read()
    lines = text.splitlines()
    sar1 = []
    sar2 = []
    print(lines)
    for x in lines:
        sar1.append(",",15)[2]
        sar2.append(",",15)[3]
    print(sar1,sar2)