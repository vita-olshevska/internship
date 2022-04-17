import random
import string


DIGITS = string.digits
UPPER_LETTERS = string.ascii_uppercase
LOWER_LETTERS = string.ascii_lowercase
PUNCTUATION = string.punctuation
PASSWORD_PARTS = [DIGITS, UPPER_LETTERS, LOWER_LETTERS, PUNCTUATION]

MIN_PASSWORD_LENGTH = 14
MAX_PASSWORD_LENGTH = 20


def decompose(number: int, count: int) -> list:
    '''
    Decompose the number into "count" positive numbers.
    :param number: what we want to decompose into the sum of some numbers
    :param count: how much numbers of the decomposition we need
    :return: decomposition of the number, which consists "count" numbers
    '''
    decomposition = []
    for i in range(1, count):
        decomposition.append(random.randint(1, number - (count - i) - sum(decomposition)))
    decomposition.append(number - sum(decomposition))
    return decomposition


def create_password(list_of_parts: list, list_of_lengths: list) -> str:
    '''
    Create a password.
    :param list_of_parts: list of strings from  which we choose characters to our password
    :param list_of_lengths: every element in this list is a number of chosen characters of corresponding string
    :return: password
    '''
    password_list = []
    for part, number in zip(list_of_parts, list_of_lengths):
        password_list += [random.choice(part) for _ in range(number)]

    random.shuffle(password_list)
    return "".join(password_list)


password_length = random.randint(MIN_PASSWORD_LENGTH, MAX_PASSWORD_LENGTH)
decomposition_of_length = decompose(password_length, len(PASSWORD_PARTS))
password = create_password(PASSWORD_PARTS, decomposition_of_length)

print(password)
