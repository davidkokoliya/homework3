name = input('Enter your Name')
surname = input('Enter your Lastname')
year = input('Enter your year of birth')
city = input('Enter your city')
email = input('Enter your email')
telephone = input('Enter your telephone number')


def my_func(name, surname, year, city, email, telephone):
    return ' '.join([name, surname, year, city, email, telephone])
print(my_func(surname, name , year , city , email , telephone ))
