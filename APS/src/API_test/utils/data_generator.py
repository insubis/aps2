from faker import Faker 
 
fake = Faker() 
 
def generate_user_data(): 
    return { 
        "name": fake.first_name(), 
        "job": fake.job() 
    } 
 
def generate_email(): 
    return fake.email() 
