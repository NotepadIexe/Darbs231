with open("C:/Users/STUDENT/Downloads/aw_pilseta.csv", "r", encoding="utf-8") as file:
    text = file.read()
    lines = text.splitlines()
    sar1 = []
    sar2 = []
    sar3 = []
    print(lines)
    for x in lines:
        sar1.append(x.split(",")[2])
        sar2.append(x.split(",")[13])
        sar3.append(x.split(",")[14])
    print(sar1, sar2, sar3)