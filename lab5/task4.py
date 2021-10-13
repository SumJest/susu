while True:
    purchase_amount = int(input())

    rubles = purchase_amount // 100
    penny = purchase_amount % 100

    if rubles > 0:
        if 5 <= rubles % 10 <= 9 or rubles % 10 == 0 or 10 <= rubles % 100 <= 20:
            print(str(rubles) + " РУБЛЕЙ")
        elif rubles % 10 == 1:
            print(str(rubles) + " РУБЛЬ")
        else:
            print(str(rubles) + " РУБЛЯ")

    if penny > 0:
        if 5 <= penny % 10 <= 9 or penny % 10 == 0 or 10 <= penny <= 20:
            print(str(penny) + " КОПЕЕК")
        elif penny % 10 == 1:
            print(str(penny) + " КОПЕЙКА")
        else:
            print(str(penny) + " КОПЕЙКИ")
