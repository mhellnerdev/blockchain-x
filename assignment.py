# user_name = 'Mark'
# user_age = 39

user_name = input('Enter your name: ')
user_age = input('Enter your age: ')

def print_user_data():
    print(user_name + ' - ' + user_age)

print_user_data()

def print_concatenated_data(el1, el2):
    print(el1 + ' - ' + el2)

print_concatenated_data(user_name, user_age)

def calculate_decades(age):
    decades_lived = age // 10
    return(decades_lived)

decades = calculate_decades(int(user_age))
print(decades)