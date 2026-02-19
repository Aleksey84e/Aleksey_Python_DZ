from address import Address
from mailing import Mailing

to_address = Address("123456", "Ставрополь", "Ленина", "10", "25")
from_address = Address("654321", "Краснодар", "Мира", "5", "15")

mailing = Mailing(
    to_address=to_address,
    from_address=from_address,
    cost=1050,
    track="TRACK123456789"
)

print(f"Отправление {mailing.track} из {mailing.from_address.city} в {mailing.to_address.city}. Стоимость {mailing.cost} рублей.")