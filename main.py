from enum import Enum
from datetime import datetime


class Role(Enum):
    Client = 1, "Клиент"
    Driver = 2, "Водитель"

class User:
    def __init__(self, id: int, name: str, phone: int, role: Role):
        self.id = id
        self.name = name
        self.phone = phone
        self.role = role

    def __str__(self):
        return f'{self.id} - {self.name} -  {self.phone} - {self.role.value[1]}'

    def __repr__(self):
        return self.__str__()
# user = User(1,"hhh",999, Role.Client)
# print(user)
class Status(Enum):
    Waiting = 1, "В ожидании"
    Coming = 2, "В пути"
    Go = 3, "Едем"


class TypePayment(Enum):
    Cash = 1, "Наличные"
    Card = 2, "Карта"
    TransferPhone = 3, "Переводом"


class Order:
    def __init__(self, id: int, price: int, status: Status, type_of_payment: TypePayment, client: User, driver: User,
                 datetime: datetime = datetime.now()):
        self.id = id
        self.datetime = datetime
        self.status = status
        self.price = price
        self.type_of_payment = type_of_payment
        self.client = client
        self.driver = driver

    def __str__(self):
        return f'{self.id} - {self.datetime} -  {self.status.value[1]} - {self.price} - {self.type_of_payment.value[1]}\n {self.client}\n {self.driver} '

    def __repr__(self):
        return self.__str__()


class Address:
    def __init__(self, id: int, address_name: str, address_name2: str):
        self.id = id
        self.id = self.id
        self.address_name = address_name
        self.address_name2 = address_name2

    def __str__(self):
        return f'{self.id} - {self.address_name} ----> {self.address_name2}'

    def __repr__(self):
        return self.__str__()


class OrderAddress:
    def __init__(self, id: int, order_id: int, address_id: int, additional_address_id: int):
        self.id = id
        self.order_id = order_id
        self.address_id = address_id
        self.additional_address_id = additional_address_id

    def __str__(self):
        return f'{self.id} - {self.order_id} - {self.address_id} - {self.additional_address_id}'

    def __repr__(self):
        return self.__str__()


class OrderHistory:
    def __init__(self, id: int,  order: Order,
                 datetime_end: datetime = datetime.now()):
        self.id = id
        self.datetime_start = order.datetime
        self.datetime_end = datetime_end
        self.status = order.status
        self.price = order.price
        self.type_of_payment = order.type_of_payment
        self.client_id = order.client.id
        self.driver_id = order.driver.id

    def __str__(self):
        return f'{self.id} - {self.datetime_start} - {self.datetime_end} -  {self.status.value[1]} - {self.price} - {self.type_of_payment.value[1]} - {self.client_id} - {self.driver_id} '

    def __repr__(self):
        return self.__str__()


class Mark(Enum):
    BMW = 1, "BMW"
    Audi = 2, "Audi"
    Mercedes = 3, "Mercedes"
    Tesla = 4, "Tesla"


class Car:
    def __init__(self, id: int, plate_number: str, mark: Mark, driver: User):
        self.id = id
        self.plate_number = plate_number
        self.mark = mark
        self.driver = driver
        self.driver_id = driver.id

    def __str__(self):
        return f'{self.id} - {self.plate_number} -  {self.mark} -  {self.driver}'

    def __repr__(self):
        return self.__str__()


class Repository:
    __users = {}
    __orders = {}
    __addresses = {}
    __orders_addresses = {}
    __orders_history = {}
    __cars = {}

    @staticmethod
    def AddUser(user: User):
        Repository.__users[user.id] = user

    @staticmethod
    def GetUser(id: int):
        return Repository.__users.get(id)

    @staticmethod
    def AddOrder(order: Order):
        Repository.__orders[order.id] = order

    @staticmethod
    def GetOrder(id: int):
        return Repository.__orders.get(id)

    @staticmethod
    def AddAddress(address: Address):
        Repository.__addresses[address.id] = address

    @staticmethod
    def GetAddress(id: int):
        return Repository.__addresses.get(id)

    @staticmethod
    def AddOrderAddress(order_address: OrderAddress):
        Repository.__orders_addresses[order_address.id] = order_address

    @staticmethod
    def GetOrderAddress(id: int):
        return Repository.__orders_addresses.get(id)

    @staticmethod
    def AddOrderHistory(order_history: OrderHistory):
        Repository.__orders_history[order_history.id] = order_history

    @staticmethod
    def GetOrderHistory(id: int):
        return Repository.__orders_history.get(id)

    @staticmethod
    def AddCar(car: Car):
        Repository.__cars[car.id] = car

    @staticmethod
    def GetCar(id: int):
        return Repository.__cars.get(id)

user_alina = User(1,"Alinus", "89247524294", Role.Client)
user_pavel = User(1,"Pavlus", "89299292929", Role.Driver)
Repository.AddUser(user_alina)
print(Repository.GetUser(1))

Repository.AddOrder(Order(1, "500 руб.", Status.Go, TypePayment.Cash, user_alina, user_pavel))
print(f'ЗАКАЗ \n {Repository.GetOrder(1)} ')

Repository.AddAddress(Address(1, "Свободный проспект 76Н", "Академика Киренского 26"))
print(f'Адрес: {Repository.GetAddress(1)}')

car1 = Car(1,"123ABC", Mark.Audi, user_pavel)
Repository.AddCar(car1)
print(f'Машина: {Repository.GetCar(1)}')

# Repository.AddOrderAddress(OrderAddress(1, 1, 1, 1))
# print(f'Адрес: {Repository.GetOrderAddress(1)}')

# Repository.AddUser(User(1,"Alinus", "89247524294", Role.Client))
# print(Repository.GetUser(1))