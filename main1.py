from task1 import Account


def main():
    account = Account('renata', 700, '1234567890', 'admin')
    account.set_passport('09876532', 'ohohohohoh')
    account.set_passport('09876532', 'admin')
    account.change_balance(300)
    account.change_balance(-5000)
    try:
        account.del_passport('admin')
    except:
        print('Паспорт был удален!!!')


main()