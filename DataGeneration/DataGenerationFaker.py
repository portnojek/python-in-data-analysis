from faker import Faker

fake = Faker()
data = [{'name': fake.name(), 'age': fake.random_int(18, 80)} for _ in range(100)]

print(data)