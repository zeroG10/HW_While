def three_argument (number_1, number_2, number_3):
    while number_1 < number_2:
        if number_3 <= 0:
            number_3 = int(input('Please enter a third argument greater than zero: '))
        number_1 += number_3
        if number_1 > number_2:
            print('Argument one:', number_1, '- MORE than argument two:', number_2)
            break
        elif number_1 == number_2:
            print('Argument one:', number_1, '- EQUALLY to argument two:', number_2)
            break
    else:
        if number_1 > number_2:
            print('The first argument:', number_1, '(on input) - GREATER than the second number:', number_2,
                  '\n' 'Please enter correct arguments.')
        elif number_1 == number_2: \
                print('The first argument:', number_1, '(on input) - is EQUAL to the second argument:', number_2,
                      '\n' 'Please enter correct arguments.')
    # return number_1

x = three_argument(4, 99, 2)

# print(x)
