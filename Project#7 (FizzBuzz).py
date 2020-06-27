def fizz_buzz_or_not_fizz_buzz(number):
    is_FizzBuzz = number % 3 == 0 & number % 5 == 0
    is_Fizz = number % 3 == 0
    is_Buzz = number % 5 == 0
    if is_FizzBuzz:
        return('FizzBuzz')
    elif is_Fizz:
        return('Fizz')
    elif is_Buzz:
        return('Buzz')
    else:
        return(number)

for number in range(1, 101):
    print(fizz_buzz_or_not_fizz_buzz(number))





