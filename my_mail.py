import string
import random


def get_mail(first,last):
    mail = first + last
    return mail
    
def get_password(size):
    password=''
    p = string.ascii_letters  
    for i in range(size):
         p = random.choice(p)
         q = password + p
         return q
    
    
a = str(input('your first name'))
b = str(input( ' your last name '))
your_mail = get_mail(a,b)
print('your_mail')

size = int(input('length of your password'))
my_password = get_password(size)
print(my_password)
