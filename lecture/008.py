# 008.py
# if, elif, else

score = 91
money = 0

if score >= 90:
    print('mom: i\'m so happy')
    money += 1000000
elif score >= 80:
    print('mom: i\'m happy')
    money += 100000
elif score >= 70:
    print('mom: happy')
    money += 10000
else:
    money += 1000
    
print(money)
