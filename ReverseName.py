import utils


def inputData():
    firstName = str(input('Enter your First Name: '))
    lastName = str(input('Enter your Last Name : '))
    return firstName, lastName


def main():
    print('Reverse Name Program')
    print('This program is designed to accepts the user\'s first and last name and print them in reverse order with a '
          'space between them.')
    data = inputData()
    print(utils.NameInReverse(data[0], data[1]))


main()
