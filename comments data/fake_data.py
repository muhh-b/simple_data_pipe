from faker import Faker

# generate French comment data in a CSV file
def generate_fake_data():
    fake = Faker('fr_FR')
    with open('fake_data.csv', 'w', encoding='utf-8') as file:  # Specify encoding
        file.write('comment\n')
        for _ in range(100):
            file.write(f'{fake.text()}\n')
            
generate_fake_data()
