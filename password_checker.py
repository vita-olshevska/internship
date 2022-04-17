import string
import argparse


DIGITS = set(string.digits)
UPPER_LETTERS = set(string.ascii_uppercase)
LOWER_LETTERS = set(string.ascii_lowercase)
PUNCTUATION = set(string.punctuation)

parser = argparse.ArgumentParser(description="Check some password")
parser.add_argument('password', type=str, nargs="+", help="The string, which we want to check. "
                                                          "Note: if multiple spaces are important, use \"quotes\"")
args = vars(parser.parse_args())
password = ' '.join(args['password'])

password_symbols = set(password)
message = {}

if not (password_symbols & UPPER_LETTERS and password_symbols & LOWER_LETTERS):
    message["up_low_letters"] = "- Password must contain both lowercase and uppercase characters"
if not password_symbols & DIGITS:
    message["digits"] = "- Password must contain digits"
if not password_symbols & PUNCTUATION:
    message["punctuations"] = f"- Password must contain at least one punctuation character ({''.join(PUNCTUATION)})"
if len(password) < 14:
    message["length"] = "- Password must be at least 14 characters long"

if message:
    print("Weak password:")
    for val in message.values():
        print(val)
else:
    print("Strong password")
