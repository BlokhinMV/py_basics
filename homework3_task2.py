def my_func(**kwargs):
    return kwargs

name = input('Enter name: ')
surname = input('Enter surname: ')
b_date = input('Enter birth date: ')
city = input('Enter city of living: ')
email = input('Enter E-mail: ')
phone = input('Enter phone number: ')

print(my_func(Username = name, User_Surname = surname, Birth_date = b_date, City_of_living = city, E_mail = email, Phone_number = phone))
