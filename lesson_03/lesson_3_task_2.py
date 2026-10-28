from smartphone import Smartphone

catalog = []

catalog.append(Smartphone("Apple", "iPhone 13", "+79123456789"))
catalog.append(Smartphone("Samsung", "Galaxy S21", "+79234567890"))
catalog.append(Smartphone("Xiaomi", "Redmi Note 10", "+79345678901"))
catalog.append(Smartphone("Nokia", "3310", "+79456789012"))

for phone in catalog:
    print(f"{phone.brand} - {phone.model}. {phone.phone_number}")
