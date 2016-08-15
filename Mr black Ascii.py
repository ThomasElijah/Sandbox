LOWER_LIMIT = 33
UPPER_LIMIT = 127
def main():

    character = str(input("Enter a character"))
    print("The ascii code for {} is {}".format(character, ord(character)))

    number = get_number(LOWER_LIMIT, UPPER_LIMIT)
    #while number < LOWER_LIMIT or number > UPPER_LIMIT:
    #    number = int(input("Enter a number between {} and {}".format(LOWER_LIMIT, UPPER_LIMIT)))
    print("The character for {} is {}".format(number, chr(number)))

    print("{:<5}{:>}".format(ord(character), chr(number)))

def get_number(lower, upper):
    num = int(input("Enter a number between {} and {}".format(lower, upper)))
    while num < lower and num > upper:
        num = input("Enter a valid number!\nEnter a number between {} and {}".format(lower, upper))
    return num

main()