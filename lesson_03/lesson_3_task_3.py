from address import Address
from mailing import Mailing

sender_address = Address("101000", "Москва", "Тверская", "1", "15")
receiver_address = Address("190000", "Санкт-Петербург", "Невский проспект", "10", "42")

my_mailing = Mailing(
    to_address=receiver_address,
    from_address=sender_address,
    cost=350,
    track="RU123456789"
)

print(f"Отправление {my_mailing.track} из {my_mailing.from_address.index}, {my_mailing.from_address.city}, {my_mailing.from_address.street}, {my_mailing.from_address.house} - {my_mailing.from_address.apartment} в {my_mailing.to_address.index}, {my_mailing.to_address.city}, {my_mailing.to_address.street}, {my_mailing.to_address.house} -{my_mailing.to_address.apartment}. Стоимость {my_mailing.cost} рублей.")