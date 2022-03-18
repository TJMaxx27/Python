count = 0
ticket = int(input('Введите количество билетов которое хотите приобрести: '))
price_25 = 990
price_out = 1390
for i in range(ticket):
    age = int(input(f'Укажите возраст {i+1}-го посетителя: '))
    if age < 18:
        count = count + 0
    if 25 >= age >=18:
        count = count + price_25
    if age > 25:
        count = count + price_out
if ticket > 3:
    count = count/1.10
    print (f"Сумма к оплате с учетом 10% скидки при покупке более 3-х билетов: {round(count)}")
else:
    print(f"Сумма к оплате: {count}")

