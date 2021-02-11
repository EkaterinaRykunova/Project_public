n=int(input("Сколько билетов вам нужно\n"))
s=0
for i in range(n):
    a=int(input("Возраст участника"))
    if a<18:
        s=s+0
    elif 18<=a<=25:
        s=s+990
    else:
        s=s+1390
if n>3:
    s=s*0.9
    print("Сумма оплаты", s)
