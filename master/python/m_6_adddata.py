f = open("인공지능캠프.txt",'a')
for i in range(6, 11):
    data = "%d번째 줄입니다.\n" % i
    f.write(data)
f.close()