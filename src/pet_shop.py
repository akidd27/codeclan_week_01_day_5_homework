# WRITE YOUR FUNCTIONS HERE
def get_pet_shop_name(pet_shop):
    return pet_shop['name']

def get_total_cash(pet_shop):
    return pet_shop['admin']['total_cash']

def add_or_remove_cash(pet_shop, cash_amount):
    pet_shop['admin']['total_cash'] += cash_amount

def get_pets_sold(pet_shop):
    return pet_shop['admin']['pets_sold']

def increase_pets_sold(pet_shop, number_to_add):
    pet_shop['admin']['pets_sold'] += number_to_add

def get_stock_count(pet_shop):
    return len(pet_shop['pets'])

def get_pets_by_breed(pet_shop, breed):
    pets_of_breed = []
    for pet in pet_shop['pets']:
        if pet['breed'] == breed:
            pets_of_breed.append(pet)
    return pets_of_breed

def find_pet_by_name(pet_shop, name):
    for pet in pet_shop['pets']:
        if pet['name'] == name:
            return pet
    return None

def remove_pet_by_name(pet_shop, name):
    pet_list_index = 0
    for pet in pet_shop['pets']:
        if pet['name'] == name:
            pet_shop['pets'].pop(pet_list_index)
        else:
            pet_list_index += 1

def add_pet_to_stock(pet_shop, new_pet):
    pet_shop['pets'].append(new_pet)

def get_customer_cash(customer):
    return customer['cash']

def remove_customer_cash(customer, cash):
    customer['cash'] -= cash

def get_customer_pet_count(customer):
    return len(customer['pets'])

def add_pet_to_customer(customer, pet):
    customer['pets'].append(pet)

def customer_can_afford_pet(customer,pet):
    if customer['cash'] >= pet['price']:
        return True
    else:
        return False

def sell_pet_to_customer(pet_shop, pet, customer):
    if pet and customer_can_afford_pet(customer, pet):
        add_pet_to_customer(customer, pet)
        remove_pet_by_name(pet_shop, pet['name'])
        customer['cash'] -= pet['price']
        pet_shop['admin']['total_cash'] += pet['price']
        pet_shop['admin']['pets_sold'] += 1


