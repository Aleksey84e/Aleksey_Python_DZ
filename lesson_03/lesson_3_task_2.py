from smartphone import Smartphone

catalog = [

Smartphone("Samsung", "Galaxy S24", "+79123456789"),
Smartphone("Apple", "iPhone 15", "+79234567890"),
Smartphone("Xiaomi", "Redmi Note 13", "+79345678901"),
Smartphone("Google", "Pixel 8", "+79456789012"),
Smartphone("OnePlus", "12", "+79567890123")
]
for smartphone in catalog:
    print(f"{smartphone.brand} - {smartphone.model}. {smartphone.number}")