import pip._vendor.distlib.compat
import time


print("                                                                                             ")
print("*-------------------------------------------------------------------------------------------*")
print("|                                        ___   ___  ___                                     |")
print("|             /\    / |     |  /\   /\  |___) |___ |___)                                    |")
print("|            /  \  /  |_____| /  \/   \ |___) |___ |  \                                     |")
print("|         ____  ____                                    ____       |                        |")
print("|        |     |    |  /\    /                        |       /_\  |                        |")
print("|        |____ |____| /  \  /                         |____  /   \ |___                     |")
print("|                                                                                           |")
print("*-------------------------------------------------------------------------------------------*")

time.sleep(2)


def conversion():
    def dec_bin(num):
        print(bin(num).replace("0b", ""))

    def dec_hex(num):
        print(hex(num).replace("0x", ""))

    def dec_oct(num):
        print(oct(num).replace("0o", ""))

    def bin_dec(num):
        print(int(num, 2))

    def bin_hex(num):
        print(hex(num).replace("0x", ""))

    def bin_oct(num):
        print(oct(num).replace("0o", ""))

    def hex_dec(num):
        print(int(num, 16))

    def hex_bin(num):
        dec = int(num, 16)
        print(bin(dec).replace("0b", ""))

    def hex_oct(num):
        deca = int(num, 16)
        print(oct(deca).replace("0o", ""))

    def oct_dec(num):
        print(int(num, 8))

    def oct_bin(num):
        print(bin(num).replace("0b", ""))

    def oct_hex(num):
        dec = int(num, 8)
        print(hex(dec).replace("0x", ""))

    def num_option1():
        print('1. Decimal')
        print('2. Hexadecimal')
        print('3. Octal')

        option = input("In which form you want to convert??\n Select the number: ")

        if option == "1":
            bin_dec(num)
        elif option == "2":
            bin_hex(int(num))
        elif option == "3":
            bin_oct(int(num))

    def num_option2():
        print('1. Binary')
        print('2. Hexadecimal')
        print('3. Octal')

        option = input("In which form you want to convert??\n Select the number: ")

        if option == "1":
            dec_bin(int(num))
        elif option == "2":
            dec_hex(int(num))
        elif option == "3":
            dec_oct(int(num))

    def num_option3():
        print('1. Binary')
        print('2. Decimal')
        print('3. Octal')

        option = input("In which form you want to convert??\n Select the number: ")

        if option == "1":
            hex_bin(num)
        elif option == "2":
            hex_dec(num)
        elif option == "3":
            hex_oct(num)

    def num_option4():
        print('1. Binary')
        print('2. Decimal')
        print('3. Hexadecimal')

        option = input("In which form you want to convert??\n Select the number: ")

        if option == "1":
            oct_bin(int(num))
        elif option == "2":
            oct_dec(num)
        elif option == "3":
            oct_hex(num)

    num = pip._vendor.distlib.compat.raw_input("Enter the number: ")

    print('1. Binary')
    print('2. Decimal')
    print('3. Hexadecimal')
    print('4. Octal')

    num_option = input("Your number is in which form??\n Select the number: ")

    if num_option == "1":
        num_option1()
    elif num_option == "2":
        num_option2()
    elif num_option == "3":
        num_option3()
    elif num_option == "4":
        num_option4()

    print("Thank you!!")


def calculation():
    def add_bin(num1, num2):
        print(bin(int(num1, 2) + int(num2, 2)).replace("0b", ""))

    def sub_bin(num1, num2):
        print(bin(int(num1, 2) - int(num2, 2)).replace("0b", ""))

    def add_hex(num1, num2):
        print(hex(int(num1, 16) + int(num2, 16)).replace("0x", ""))

    def sub_hex(num1, num2):
        print(hex(int(num1, 16) - int(num2, 16)).replace("0x", ""))

    def add_oct(num1, num2):
        print(oct(int(num1, 8) + int(num2, 8)).replace("0b", ""))

    def sub_oct(num1, num2):
        print(oct(int(num1, 8) - int(num2, 8)).replace("0b", ""))

    def add_dec(num1, num2):
        print(float(num1) + float(num2))

    def sub_dec(num1, num2):
        print(float(num1) - float(num2))

    print('1. Binary')
    print('2. Decimal')
    print('3. Hexadecimal')
    print('4. Octal')

    print("Your number is in which form?? \n Select the number accordingly: \n")
    opt = input("")

    if opt == "1":
        num1 = input("Enter first number: ")
        operator = input("Enter operator: ")
        num2 = input("Enter second number: ")

        if operator == '+':
            add_bin(num1, num2)
        elif operator == '-':
            sub_bin(num1, num2)
        else:
            print('Invalid Operator!!')

    elif opt == "2":
        num1 = float(input("Enter first number: "))
        operator = input("Enter operator: ")
        num2 = float(input("Enter second number: "))

        if operator == '+':
            add_dec(num1, num2)
        elif operator == '-':
            sub_dec(num1, num2)
        else:
            print('Invalid Operator!!')

    elif opt == "3":
        num1 = input("Enter first number: ")
        operator = input("Enter operator: ")
        num2 = input("Enter second number: ")

        if operator == '+':
            add_hex(num1, num2)
        elif operator == '-':
            sub_hex(num1, num2)
        else:
            print('Invalid Operator!!')

    elif opt == "4":
        num1 = float(input("Enter first number: "))
        operator = input("Enter operator: ")
        num2 = float(input("Enter second number: "))

        if operator == '+':
            add_oct(num1, num2)
        elif operator == '-':
            sub_oct(num1, num2)
        else:
            print('Invalid Operator!!')


def start():
    print("You want to convert or calculate?? \n Type 'con' to CONVERT and 'cal' to CALCULATE: ")

    selection = input(">>")

    if selection == str('con'):
        conversion()
    elif selection == str('cal'):
        calculation()
    else:
        print("Invalid Input!!")


def quit():
    print("Thank you!!!")
    quit()


start()

time.sleep(2)
print('Again?')
print('Y or N')
re = input('>>')

if re == str('y') or str('Y'):
    start()
elif re == str('n') or str('N'):
    quit()
