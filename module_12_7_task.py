per_cent = {'ТКБ': 5.6, 'СКБ': 5.9, 'ВТБ': 4.28, 'СБЕР': 4.0}
depo=list((per_cent.values()))
money=float(input("Введите сумму вклада"))
depos=money/100*depo[0],money/100*depo[1], money/100*depo[2], money/100*depo[3]
deposit=list(depos)
print("Максимальная сумма, которую вы сможете заработать - ", int(max(deposit)))
