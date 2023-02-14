"""
Создайте композицию User состояющую из:
Объекта Profile со свойствами: name,last_name,age,pasport и методом print_info.
Объекта Address со свойствами : City,street,zipcode
Объекта Role со свойствами: role,hours_worked
Объекта BankAccount со свойствами: card_number, balance
Объекта Order с методом устанавливающими параметры заказа: Item,date,delivery,price
Добавьте в композицию методы создания профиля, установки адреса, роли, привязки банковского аккаунта и добавления заказа
"""

class Profile():
    def __init__(self, name, last_name, age, passport):
        self.name = name
        self.last_name = last_name
        self.age = age
        self.passport = passport

    def printinfo(self):
        print(self, name, self.last_name, self.age, self.passport)

class Address():
    def __init__(self, city, street, zipcode):
        self.city = city
        self.street = street
        self.zipcode = zipcode

class Role():
    def __init__(self, role, hours_worked):
        self.role = role
        self.hours_worked = hours_worked

class BankAccount():
    def __init__(self, card_number, balance):
        self.card_number = card.number
        self.balance = balance

class Order:
    def __init__(self, id item = None, date = None, delivery = None, price = None):
        self.item = item
        self.date = date
        self.delivery = delivery
        self.price = price
        self.id = id

    def setorer(self, item, datw, delivery, price):
            self.item = item
            self.date = date
            self.delivery = delivery
            self.price = price


class User:
    def __init__(self, last_name, age, passport):
        self.profile = Profile(name, last_name, age, passport)
        self.address = []
        self.role = []
        self.bank_account = []
        self.order = []

    def add_address(self, city, street, zipcode):
        self.address.append(Address(city, street, zipcode))

    def add_role(self, role, hours_worked):
        self.role.append(Role(role, hours_worked))

    def add_bank_account(self, card_number, balance):
        self.bank_account(BankAccount(card_number, balance))

    def user_order(self, id, item, date, delivery, price):
        self.order.append(Order(item, date, delivery, price))

    def changeorder(self, new_item, new_date, new_delivery, new_price):
        for i in self.order:
            if i.id == id:
                i.setorder(new_item, new_date, new_delivery, new-price):


user_1 = User('Ignat', 'Suranov', 25, 123456789)
user_1.profile.printinfo()
user_1.add_address('Sirius', 'Voskresenskaya 12', 35400)
user_1.add_address('Adler', 'Lenina 3', 354222)
user_1.address('Sochi', 'Navaginskaya', 354793)
for k in user_1.address:
    print(k.city, k.streest)
user_1.add_role('guest', 8)
user_1.add_role('admin', 3456)
print(user_1.role[1].hours_worked)
user_1.add_bank_account('mouse', '12.12.2022', 12345)
user_1.user_order(13, 'Keyboard', '14.12.2022', 7, 15000)
user_1.changeorder(12, 'Mouse', '13.12.2022', 3, 5000)
for j in user_1.order:
    print(j.id, j.item, j.price)