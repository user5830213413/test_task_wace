import requests
import random

# ???? СОЗДАНИЕ ПОЛЬЗОВАТЕЛЯ

# data = {
#     'login': 'Вася',
#     'password': '1234'
# }

# response = requests.post('http://127.0.0.1:5000/user/register', json=data)

# print(response.json())



# ???? СОЗДАНИЕ КОШЕЛЬКА

# data = {
#     'login': 'Петя',
#     'address': '0x' + ''.join([random.choice('0123456789ABCDEF') for i in range(40)]),
#     'net': 'ETH'
# }

# response = requests.post('http://127.0.0.1:5000/wallet', json=data)

# print(response.json())


# # ??? ИЗМЕНЕНИЕ КОШЕЛЬКА
# data = {
#     'login': 'Петя',
#     'address': '0xB17C95A96086DA0644295819BA177B14A9E0996D',
#     'operation': 'addition',
#     'summ': 5000
# }

# response = requests.put('http://127.0.0.1:5000/wallet/transfer', json=data)

# print(response.json())



# ???? ПЕРЕВОД СРЕДСТВ


# data = {
#     'login': 'Петя',
#     'from_address': '0xB17C95A96086DA0644295819BA177B14A9E0996D',
#     'to_address': '0x14EDB814CA88E502FD17CA9B9FE4E69D7C40143E',
#     'summ': 1000
# }

# response = requests.post('http://127.0.0.1:5000/wallet/transfer', json=data)

# print(response.json())


# ???? ПОЛУЧЕНИЕ ВСЕХ КОШЕЛЬКОВ ПОЛЬЗОВАТЕЛЯ 

# response = requests.get('http://127.0.0.1:5000/wallet/1')

# print(response.json())



# ???? УДАЛЕНИЕ ПОЛЬЗОВАТЕЛЯ
# response = requests.delete('http://127.0.0.1:5000/user/1')

# print(response.json())


# ??? ИЗМЕНЕНИЕ ПОЛЬЗОВАТЕЛЯ
# data = {
#     'login': 'ВАСЯ2',
#     'password': '5656'
# }

# response = requests.put('http://127.0.0.1:5000/user/2', json=data)

# print(response.json())