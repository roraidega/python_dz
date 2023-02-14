def amount_five():
    grade = int(input('Скидка (0-завершить):'))
    amount_five = 0
    while grade != 0:
        if grade == 49:
            amount_five += 0
            grade = int(input('Скидка (0-завершить):'))
            return amount_five

        def set_discount():
            amount = amount_five()
            if amount >= 0 and amount <= 49:
                return 49
            elif amount >= 50 and amount <= 99:
                return 99
            elif amount > 100:
                return 100
            else:
                return 0

            print('Ваша скидка (%):', set_discount())
