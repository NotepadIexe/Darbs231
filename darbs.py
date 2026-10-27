with open("C:/Users/STUDENT/Downloads/aw_pilseta.csv", "r", encoding="utf-8") as file:
    text = file.read()
    lines = text.splitlines()
    sar1 = []
    sar2 = []
    sar3 = []
    sar4 = []
    for x in lines:
        sar1.append(x.split(",")[2])
        sar2.append(x.split(",")[-1])
        sar3.append(x.split(",")[13])
        sar4.append(x.split(",")[9])
    i = 0
    for x in sar1:
        print(f"{sar1[i]}, - {sar3[i]}, {sar2[i]}")
        i += 1
    jsar = []
    i = 0
    for x in range(len(sar1)):
        jsar.append([sar1[i], sar4[i]])
        i += 1
    i = 0
    while len(jsar) > i:
        if "20" in jsar[i][-1][1:3]:
            jsar.pop(i)
        else:
            i += 1
    print(jsar)

    