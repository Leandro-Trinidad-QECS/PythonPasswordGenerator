# !/usr/bin/python
import random, string,math
import time
import argparse

def generate_password(password_length,add_lowerCase,add_upperCase,add_numbers,add_specialChar,seed):
# The main function that does the generating of the passwords

    # puts system random to a variable
    randomSystem = random.SystemRandom()

    #gets all the characters on a keyboard and puts it in their on variables
    seed_lowercase_letters = string.ascii_lowercase  # abcdefghijklmnopqrstuvwxyz
    seed_uppercase_letters = string.ascii_uppercase  # ABCDEFGHIJKLMNOPQRSTUVWXYZ
    seed_numbers = string.digits                     # 0123456789
    seed_special_char = string.punctuation           # !"#$%&'()*+,-./:;<=>?@[\]^_`{|}~

    # sets up passChain
    # this is the variable that the program chooses characters from
    passChain = "" # puts the above variables in here if the user wants to

    #if the user doesnt want to use a seed
    if(seed == None or seed == ""):

        # if the options like lowercase is chosen then it adds lowercaseto the seed
        if(add_lowerCase):
            passChain += seed_lowercase_letters
        if(add_upperCase):
            passChain += seed_uppercase_letters
        if(add_numbers):
            passChain += seed_numbers
        if(add_specialChar):
            passChain += seed_special_char
    else:
        passChain = seed

    # then
    # randomly chooses from the passchain
    output_password = ""
    for i in range(password_length):
        output_password += "".join(randomSystem.choice(passChain))

    return output_password

def checkBool(name):
    # checks if the user has typed in true or false
    max_Try = 0
    while max_Try <= 3:
        user_input = input(name+ " [T/F] ")
        if user_input in ("True","T","true","t"):
            return True
        if user_input in ("False","F","false","f"):
            return False
        else:
            print("try again")
            max_Try +=1
    exit(0)
def checkbutton(input):
    if input == 1:
        return True
    return False
def checkNum(numput):
    try:
        return int(numput)
    except:
        print(numput + " is not a number")
        return 6

    exit(0)
def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('-l', action='store', dest='pass_length',
                    help='Password length',required=True)
    parser.add_argument('-lc', action='store_true', default=False,
                    dest='lowerCase_switch',required=True,
                    help='Add lowercase to passwords')
    parser.add_argument('-uc', action='store_true', default=False,
                    dest='upperCase_switch',
                    help='Add uppercase to passwords')
    parser.add_argument('-n', action='store_true', default=False,
                    dest='number_switch',
                    help='Add numbers to passwords')
    parser.add_argument('-sc', action='store_true', default=False,
                    dest='specialCharCase_switch',
                    help='Add special characters to passwords')
    parser.add_argument('-s', action='store', dest='seed',
                    help='Seed')
    results = parser.parse_args()
    length = checkNum(results.pass_length)
    lowercase = results.lowerCase_switch
    uppercase = results.upperCase_switch
    numbers = results.number_switch
    specialChar = results.specialCharCase_switch
    seed = results.seed



    print("----------  %s  ----------" % (generate_password(length,lowercase,uppercase,numbers,specialChar,seed)))

if __name__ == '__main__':
    main()
