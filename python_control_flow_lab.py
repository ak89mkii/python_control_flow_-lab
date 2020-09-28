# PROBLEM 01:

# cvcheck = input('Please enter a letter from the alphabet:')

# if cvcheck in ('a', 'e', 'i', 'o', 'u') and cvcheck.isalpha() == True and len(cvcheck) <= 1:
#     print(f'The letter {cvcheck} is a vowel')

# elif cvcheck.isalpha() == True and len(cvcheck) <= 1:
#     print(f'The letter {cvcheck} is a consonant')

# else:
#     print(f'The letter {cvcheck} is a neither')


# PROBLEM 2:

# phrase = input('Please enter a word or phrase:')
# result = len(phrase)

# if phrase != "quit":
#     print(f'What you entered is {result} characters long.')
    
# else:
#     print("exit")


# PROBLEM 3:

# humanyear = int(input("Input a dog's age in human years:"))
# dogage = humanyear * 7 + 6

# if humanyear == 1:
#     print("The dog's age in dog years is 10")

# elif humanyear == 2:
#     print("The dog's age in dog years is 20")

# else:
#     print(f"The dog's age in dog years is {dogage}")


# PROBLEM 4:

# a = int(input('Side A:'))
# b = int(input('Side B:'))
# c = int(input('Side C:'))

# if a == b and b == c:
#     print('It is equalateral.')

# elif a != b and b != c and a != c:
#     print('It is scalene.')

# else: 
#     print('It is isosceles.')

# PROBLEM 5:

# def fib(n):
#     a = 0
#     b = 1

#     print(a)
#     print(b)

#     for i in range(2,n):
#         c = a + b
#         a = b
#         b = c

#         print(f'term: {i} / number: {c}')

# fib(51)


# PROBLEM 6:

month = input('Enter the month of the year (format Jan - Dec):')
day = int(input('Enter the day of the month:'))

if month == ( 'Jan' or 'Feb'):
    print('...is in winter.')

elif month == ( 'Apr' or 'May'):
    print('...is in spring.')

elif month == ( 'Jul' or 'Aug'):
    print('...is in summer.')

elif month == ( 'Oct' or 'Nov'):
    print('...is in fall.')

elif month == ( 'Dec'):
    if day < 21:
        print('...is in fall.')
    else:
        print('...is in winter.')

elif month == ( 'Mar'):
    if day < 19:
        print('...is in winter.')
    else:
        print('...is in spring.')

elif month == ( 'Jun'):
    if day < 20:
        print('...is in spring.')
    else:
        print('...is in summer.')
    
elif month == ( 'Sep'):
    if day < 21:
        print('...is in summer.')
    else:
        print('...is in fall.')

else:
    print({"Gondor / Hoth"})


