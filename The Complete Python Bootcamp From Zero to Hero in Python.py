# if __name__ == '__main__':
#     func()

# print('Hello '+'Jose')
# print('Hello','Jose')

# sample = 'Hello World it is beautiful'

# print(sample.upper())
# print(sample.lower())
# print(sample.split())
# print(sample.split('i'))

# mylist = [1,2,3,[4,5,['target']]]
# print(mylist[3][2][0])

# d = {'k1':[1,2,3,{'tricky':['oh','man','inception',{'target':[1,2,3,'hello']}]}]}
# print(d['k1'][3]['tricky'][3]['target'][3])

# name = 'Sam'
# age = 3
# print(f'{name} is {age} years old')

# list1 = [1,2,3]
# list2 = [4,5]

# list1.append(list2)
# print(list1)

# list3 = [1,2,3]
# list4 = [4,5]

# list3.extend(list4)
# print(list3)

# name = 'Frankie'

# if name == 'Frankie':
#     print('hello Frankie')
# elif name == 'Sammy':
#     print('hello Sammy')
# else:
#     print('what is your name?')

# mylist = [(1,2,3),(5,6,7),(8,9,10)]
# for a,b,c in mylist:
#     print(c)

# name = 'hello frankie'
# print(name[1:])
# print(name[:5])
# print(name[6:8])
# print(name[-1:])
# print(name[-3:])
# print(name[::-1])
# print(name[::-3])

# tweet = 'Go Flames! Go'
# print(tweet.split('!'))
# print(tweet.split('!')[1].strip())
# print(tweet[-2:])

# st = 'Print every word in this sentence that has an even number of letters'

# for word in st.split():
#     if len(word)%2 == 0:
#         print(word)

# for num in range(1,101):
#     if num%3 == 0 and num%5 == 0:
#         print('FizzBuzz')    
#     elif num%3 == 0:
#         print('Fizz')
#     elif num%5 == 0:
#         print('Buzz')
#     else:
#         print(num)

# st = 'Create a list of the first letters of every word in this string'

# print([word[0] for word in st.split()])


# def myfunc(*args):
#     result = []
#     for num in args:
#         if num%2 == 0:
#             result.append(num)
#     return result

# print(myfunc(1, 2, 3, 4, 6))


# '''
# You are driving a little too fast, and a police officer stops you. Write a function to return one of 3 possible results: "No ticket", "Small ticket", or "Big Ticket". 
# If your speed is 60 or less, the result is "No Ticket". If speed is between 61 and 80 inclusive, the result is "Small Ticket". If speed is 81 or more, the result is "Big Ticket". 
# Unless it is your birthday (encoded as a boolean value in the parameters of the function) -- on your birthday, your speed can be 5 higher in all cases.
# '''

# def caught_speeding(speed, is_birthday):
#     if is_birthday:
#         speed -= 5

#     if speed > 80:
#         return 'big ticket'
#     elif speed > 60:
#         return 'small ticket'
#     else:
#         return 'no ticket'
    
# print(caught_speeding(61, False))


# def paper_doll(text):
#     result = ''
#     for char in text:
#         result += char * 10
#     return result

# print(paper_doll('hello'))


# class Account():

#     def __init__(self,owner,balance=0):
#         self.owner = owner
#         self.balance = balance

#     def deposit(self,deposit_amount):
#         self.balance += deposit_amount
#         print(f'Added ${deposit_amount} to the balance')
#         print(f'Current balance is ${self.balance}')

#     def withdrawn(self,withdraw_amount):
#         if self.balance >= withdraw_amount:
#             self.balance -= withdraw_amount
#             print(f'Withdrew ${withdraw_amount} from the balance')
#             print(f'Current balance is ${self.balance}')
#         else:
#             print('Funds unavailable')

#     def __str__(self):
#         return f'Account owner: {self.owner} \nAccount balance: ${self.balance}'
    
# acct = Account('Jose',100)

# print(acct)

# acct.deposit(100)

# acct.withdrawn(100)

# acct.withdrawn(300)


# import requests, bs4, sys
# sys.stdout.reconfigure(encoding='utf-8')

# url = 'https://quotes.toscrape.com/page/'
# page_still_valid = True
# authors = set()
# page = 1

# while page_still_valid:
    
#     page_url = url+str(page)
    
#     res = requests.get(page_url)
    
#     if 'No quotes found!' in res.text:
#         break # or page_still_valid = False
        
#     soup = bs4.BeautifulSoup(res.text,'lxml')
    
#     for name in soup.select('.author'):
#         authors.add(name.text)
    
#     page = page+1

# print(authors)



# from PIL import Image

# mac = Image.open('C:\\Users\\sunc\\example.jpg')

# mac.show()


# with open('myfile.txt','w') as f:
#     f.write('Hello this is a text file\n')
#     f.write('this is the second line\n')
#     f.write('this is the third line')

# with open('my_new_file.txt','w') as f:
#     f.write('ONE ON FIRST\n')
#     f.write('TWO ON SECOND\n')
#     f.write('THREE ON THIRD')

# with open('my_new_file.txt','r') as f:
#     print(f.read())

# with open('my_new_file.txt','a') as f:
#     f.write('\nFOUR ON FOURTH')

# with open('my_new_file.txt','r') as f:
#     print(f.read())

# mylist = [1,2,3,4,5,6,7,8,9,10]

# list_sum = 0

# for num in mylist:
#     list_sum += num
# print(list_sum)

# mylist = [(1,2),(3,4),(5,6),(7,8)]

# # tuple unpacking
# for a,b in mylist:
#     print(b)

# d = {'k1':1,'k2':2,'k3':3}

# for item in d.items():
#     print(item)

# for key in d.keys():
#     print(key)

# for value in d.values():
#     print(value)

# x = 0

# while x < 5:
#     print(f'The current value of x is {x}')
#     x += 1
# else:
#     print('x is not less than 5')


# for letter in 'Sammy':
#     if letter == 'a':
#         continue
#         # break
#     print(letter)

# x = 0

# while x < 5:
#     if x == 2:
#         break
#     print(x)
#     x += 1

# for num in range(0,10,2):
#     print(num)

# index_count = 0

# for letter in 'abcde':
#     print(f'At index {index_count} the letter is {letter}')
#     index_count += 1

# index_count = 0
# word = 'abcde'

# for letter in word:
#     print(word[index_count])
#     index_count += 1

# mystring = 'abcde'

# mylist = [letter for letter in mystring]
# print(mylist)

# for index,letter in enumerate(word):
#     print(f'{index}:{letter}')

# mylist1 = [1,2,3,4,5,6]
# mylist2 = ['a','b','c']
# mylist3 = [100,200,300]

# for item in zip(mylist1,mylist2,mylist3):
#     print(item)
# print('\n')
# print(list(zip(mylist1,mylist2,mylist3)))
# print('\n')
# for a,b,c in zip(mylist1,mylist2,mylist3):
#     print(b)

# from random import shuffle, randint

# mylist = [1,2,3,4,5,6,7,8,9,10]

# shuffle(mylist)
# print(mylist)
# print(randint(0,100))

# mynum = randint(0,100)
# print(mynum)

# mystring = 'hello'
# mylist = []

# for letter in mystring:
#     mylist.append(letter)
#     print(mylist)

# mystring = 'hello'

# mylist = [letter for letter in mystring]
# print(mylist)

# # alternative
# print([letter for letter in 'hello'])

# # alternative #2
# print(list('hello'))

# mylist = [num**2 for num in range(0,11)]
# print(mylist)

# mylist = [x**2 for x in range(0,11) if x%2==0]
# print(mylist)

# celsius = [0,10,20,34.5]

# fahrenheit = []

# for temp in celsius:
#     fahrenheit.append((9/5)*temp+32)
# print(fahrenheit)

# fahrenheit = [((9/5)*temp+32) for temp in celsius]
# print(fahrenheit)


# st = 'Sam Print only the words that start with s in this sentence'

# print(st.split())

# for word in st.split():
#     if word[0].lower() == 's':
#         print(word)

# mystring = [word for word in st.split() if word[0].lower() == 's']
# print(mystring)


# for num in range(0,11):
#     if num%2 == 0:
#         print(num)

# print([num for num in range(0,51) if num%3 == 0])


# st = 'Print every word in this sentence that has an even number of letters'

# for word in st.split():
#     if len(word)%2 == 0:
#         print(word)

# print([word for word in st.split() if len(word)%2 == 0])


# for num in range(0,101):
#     if num%3 == 0 and num%5 == 0:
#         print(f'FizzBuzz: {num}')
#     elif num%3 == 0:
#         print(f'Fizz: {num}')
#     elif num%5 == 0:
#         print(f'Buzz: {num}')
#     else:
#         print(num)


# st = 'Create a list of the first letters of every word in this string'

# print([word[0] for word in st.split()])


# def say_hello():
#     '''
#     docstring: purpose of this function
#     '''
#     print('hello')
#     print('are')
#     print('you')

# say_hello()


# def say_hello(name):
#     print(f'Hello {name}')

# say_hello('bitch')

# def say_hello(name='Default'):
#     print(f'Hello {name}')

# say_hello()

# def add_num(num1,num2):
#     return num1+num2

# print(add_num(10,20))

# def print_result(a,b):
#     print(a+b)

# def return_result(a,b):
#     return (a+b)

# print_result(10,20)
# print(return_result(10,20))

# result = print_result(10,20)
# returns None
# print(result)

# result = return_result(10,20)
# print(result)

# def even_check(num):
#     return num % 2 == 0

# print(even_check(10))

# def check_even_list(num_list):
#     for num in num_list:
#         if num % 2 == 0:
#             return True
#         return False

# print(check_even_list([3,4,5]))

# def check_even_list(num_list):
#     for num in num_list:
#         if num % 2 == 0:
#             return True
#     return False

# print(check_even_list([3,4,5]))


# def check_even_list(num_list):

#     even_numbers = []

#     for num in num_list:
#         if num % 2 == 0:
#             even_numbers.append(num)
#     return even_numbers

# print(check_even_list([1,2,3,4,5]))
# print(check_even_list([1,3,5]))


# # cleaner version using list comprehension
# def check_even_list(num_list):
#     return [num for num in num_list if num % 2 == 0]

# print(check_even_list([1,2,3,4,5]))
# print(check_even_list([1,3,5]))


# stock_prices = [('AAPL',200),('GOOGL',400),('MSFT',100)]

# for item in stock_prices:
#     print(item)

# for ticker,price in stock_prices:
#     print(ticker)
#     print(price)


# # return the employee with the most hours
# work_hours = [('Abby',100),('Billy',4000),('Cassie',8000)]

# def employee_check(work_hours):

#     current_max = 0
#     employee_of_month = ''

#     for employee,hours in work_hours:
#         if hours > current_max:
#             current_max = hours
#             employee_of_month = employee

#     return f'{employee_of_month} is the employee of the month with {current_max} hours'

# print(employee_check(work_hours))


# # cleaner alternative from Claude
# work_hours = [('Abby',100),('Billy',4000),('Cassie',8000)]

# def employee_check(work_hours):
#     name, hours = max(work_hours, key=lambda pair: pair[1])
#     return f'{name} is the employee of the month with {hours} hours'

# print(employee_check(work_hours))


# def myfunc(*args):
#     return sum(args) * 0.05

# print(myfunc(100,200,300,400,500))


# def myfunc(**kwargs):
#     print(kwargs)

# myfunc(fruit='apple',veggie='lettuce')


# def myfunc(**kwargs):
#     print(kwargs)
#     if 'fruit' in kwargs:
#         print(f'My fruit of choice is {kwargs['fruit']}')
#     else:
#         print('I did not find any fruit here')

# myfunc(fruit='apple',veggie='lettuce')


# def myfunc(*args,**kwargs):
#     print(args)
#     print(kwargs)
#     print(f'I would like {args[0]} {kwargs['food']}')

# myfunc(10,20,30,fruit='orange',food='eggs',animal='dog')


# def myfunc(*args):
#     result = []
#     for num in args:
#         if num % 2 == 0:
#             result.append(num)
#     return result

# print(myfunc(1,2,3,4,5,6))

# # using list comprehension instead
# def myfunc(*args):
#     result = [num for num in args if num % 2 == 0]
#     return result

# def count_dog(string):
#     count = 0
#     for word in string.lower().split():
#         if word == 'dog':
#             count += 1           
#     return count

# print(count_dog('this dog runs faster than the other dog'))

# # using list comprehension instead
# def count_dog(string):
#     return sum([word == 'dog' for word in string.lower().split()])

# print(count_dog('this dog runs faster than the other dog'))

# print(myfunc(1,2,3,4,5,6))

# my_nums = [1,2,3,4,5]

# # not common practice to assign a variable to a lambda function
# square = lambda num: num**2
# print(square(5))

# print(list(map(lambda num: num%2==0, my_nums)))
# print(list(filter(lambda num: num%2==0, my_nums)))

# print(list(map(lambda num: num**2, my_nums)))
# print(list(filter(lambda num: num**2, my_nums)))

# names = ['Andy','Eve','Sally']

# print(list(map(lambda x: x[::-1],names)))

# # return all words that don't start with s
# seq = ['soup','dog','salad','cat','great']
# print(list(map(lambda word: word[0] != 's', seq)))
# print(list(filter(lambda word: word[0] != 's', seq)))

# def up_lows(s):
#     upper_count = 0
#     lower_count = 0

#     for char in s:
#         if char.isupper():
#             upper_count += 1
#         elif char.islower():
#             lower_count += 1

#     print('No. of upper case characters: ',upper_count)
#     print('No. of lower case characters: ',lower_count)

# s = 'Hello Mr. Rogers, how are you this fine Tuesday?'
# up_lows(s)


# class Dog():
#     def __init__(self,mybreed):
#         self.my_attribute = mybreed

# my_dog = Dog(mybreed='Lab')
# print(my_dog.my_attribute)

# # don't need () at end of class name when the class is not inheriting anything 
# # can't use return in __init__
# class Dog:
#     def __init__(self,breed,name,spots):

#         self.breed = breed
#         self.name = name
#         self.spots = spots

# # it's good practice to type out the keyword arguments when there are multiple string attributes
# my_dog = Dog(breed='lab',name='Sammy',spots=False)

# print(my_dog.breed)
# print(my_dog.name)
# print(my_dog.spots)


# class Dog:
#     species = 'mammal'

#     def __init__(self,breed,name):
#         self.breed = breed
#         self.name = name

#     def bark(self,number):
#         return f'Woof! My name is {self.name} and the number is {number}'

# my_dog = Dog(breed='lab',name='Sam')

# print(my_dog.species)
# print(my_dog.breed)
# print(my_dog.name)
# print(my_dog.bark(10))


# # set optional attribute default value
# class Circle:
#     pi = 3.14

#     def __init__(self,radius=1):
        
#         self.radius = radius
#         self.area = radius * radius * Circle.pi

#     def get_circumference(self):
#         return self.radius * Circle.pi * 2

# # pi is a Class attribute (shared by all instances) in this case
# # can be accessed through the class or an instance    
# print(Circle.pi)
    
# my_circle = Circle()

# print(my_circle.pi)
# print(my_circle.radius)
# print(my_circle.area)
# print(my_circle.get_circumference())

# print('\n')

# my_circle = Circle(30)

# print(my_circle.pi)
# print(my_circle.radius)
# print(my_circle.area)
# print(my_circle.get_circumference())

# class Animal:
#     def __init__(self):
#         print('animal created')

#     def who_am_I(self):
#         print('I am an animal')

#     def eat(self):
#         print('I am eating')

# my_animal = Animal()
# my_animal.who_am_I()
# my_animal.eat()

# print('\n')

# class Dog(Animal):
#     def __init__(self):
#         Animal.__init__(self)
#         print('dog created')

#     def who_am_I(self):
#         print('I am a dog')

#     def bark(self):
#         print('woof')

# my_dog = Dog()
# my_dog.who_am_I()
# my_dog.eat()
# my_dog.bark()

# print('\n')

# # alternative using the super() function
# class Dog(Animal):
#     def __init__(self):
#         super().__init__()

#     def who_am_I(self):
#         super().who_am_I() # not needed
#         print('I am a dog')

#     def bark(self):
#         print('woof')

# my_dog = Dog()
# my_dog.who_am_I()
# my_dog.eat()
# my_dog.bark()



# class Car:
#     def __init__(self,brand,model):
#         self.brand = brand
#         self.model = model

#     def start_engine(self):
#         print(f"The {self.brand} {self.model}'s engine has started")

# car1 = Car(brand='Toyota',model='Camry')

# car1.start_engine()


# # don't need __init__ constructor method since we're not initializing any object attributes
# class Dog:
#     def speak(self):
#         return 'Woof'
    
# class Cat:
#     def speak(self):
#         return 'Meow'
    
# def make_sound(animal):
#     print(animal.speak())

# dog = Dog()
# cat = Cat()

# make_sound(dog)
# make_sound(cat)


# # Polymorphism with inheritance
# class Animal:
#     def speak(self):
#         return 'some sound'
    
# class Dog(Animal):
#     def speak(self):
#         return 'bark'
    
# class Cat(Animal):
#     def speak(self):
#         return 'meow'

# animal = Animal()    
# dog = Dog()
# cat = Cat()

# print(animal.speak())
# print(dog.speak())
# print(cat.speak())

# print('\n')

# # or alternatively:
# animals = [Animal(), Dog(), Cat()]

# for animal in animals:
#     print(animal.speak())


# # __str__ magic (dunder) method
# class Book:
#     def __init__(self,title,author):
#         self.title = title
#         self.author = author

#     def __str__(self):
#         return f'{self.title} by {self.author}'
    
# book = Book(title='1984', author='George Orwell ')
# print(book)


# class Account:
#     def __init__(self,owner,balance=0):
#         self.owner = owner
#         self.balance = balance

#     def deposit(self,deposit_amount):
#         self.balance += deposit_amount
#         print(f'Added ${deposit_amount} to the balance')
#         print(f'Current balance is ${self.balance}')

#     def withdrawn(self,withdraw_amount):
#         if self.balance >= withdraw_amount:
#             self.balance -= withdraw_amount
#             print(f'Withdrew ${withdraw_amount} from the balance')
#             print(f'Current balance is ${self.balance}')
#         else:
#             print('funds unavailable')

#     def __str__(self):
#         return f'Account owner: {self.owner} \nAccount balance: ${self.balance}'

# acct = Account(owner='Jose',balance=100)

# print(acct)
# acct.deposit(100)
# acct.withdrawn(100)


# try:
#     result = 10 + 10
#     result2 = 10 + '10'
# except:
#     print("doesn't work")
# else:
#     print(f'no issues, result is {result}')
# finally:
#     print('always run')

# Python technique that is an alternative to the for loop below, *items unpacks
# items = [1,2,3]

# print('Items are: ', *items, sep='\n')

# for item in items:
#     print(item)


# def log_decorator(func):
#     def wrapper():
#         print(f'Calling {func.__name__}()')
#         func()
#         print(f'Finished {func.__name__}()')
#     return wrapper

# @log_decorator
# def say_hello():
#     print('Hello!')

# say_hello()


# squares = (x**2 for x in range(5))
# print(next(squares))
# print(next(squares))

# # same as above
# def squares_gen():
#     for x in range(5):
#         yield x**2

# for num in squares_gen():
#     print(num)


# def count_up_to(n):
#     count = 1
#     while count <= n:
#         yield count
#         count += 1

# for num in count_up_to(10):
#     print(num)

# def create_cubes(n):
#     result = []
#     for x in range(n):
#         result.append(x**3)
#     return result

# for x in create_cubes(10):
#     print(x)

# print('\n')

# # same result
# def create_cubes_gen(n):
#     for x in range(n):
#         yield x**3

# for x in create_cubes_gen(10):
#     print(x)

# from collections import Counter

# mylist = [1,1,1,1,1,1,1,2,2,2,2,3,3,3,3,3]
# print(Counter(mylist))

# mylist = ['a','a',10,10,10]
# print(Counter(mylist))

# print(Counter('aaaaaabbbbccccccc'))

# sentence = 'How many times does each word show up in this sentence'
# print(Counter(sentence.split()))

# letters = 'aaaaaaaaabbbbbbbbbbbbcccccccccccccccccddddddddddddddddddddddddddeeeeeeeee'
# c = Counter(letters)
# print(c.most_common())
# print(c.most_common(2))

# f = open('practice.txt','w+')
# f.write('this is a test string 2')
# f.close()

# better way of writing the above, no need to use f.close()
# with open('practice.txt','w+') as f:
#     f.write('this is a test string 2')

# import os

# print(os.getcwd())
# print(os.listdir())

# import math

# print(math.floor(4.35))
# print(math.ceil(4.35))

# import re

# text = "The agent's phone number is 408-555-1234. Call soon"
# text2 = 'my phone once, my phone twice'
# pattern = 'phone'

# print(re.search(pattern,text))
# print(re.search(pattern,text2))
# print(re.findall(pattern,text2))

# print(['one','two','three'][0])

# print('hello')