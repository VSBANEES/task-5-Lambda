import re


def validate_regex(input_string, regex_pattern): #Validates if the input string matches the given regular expression pattern.
    return bool(re.fullmatch(regex_pattern, input_string)) #Returns: bool: True if the input string matches the regular expression pattern, False otherwise.


def validate_email(email): #Validates if the given string is a valid email address.
    email_regex = r'^[\w\.-]+@[a-zA-Z\d-]+\.[a-zA-Z]{2,}$' #Returns: bool: True if the email address is valid, False otherwise.
    return validate_regex(email, email_regex)
def validate_bangladeshi_mobile_number(number): #Validates if the given string is a valid mobile number of Bangladesh.

    mobile_regex = r'^\+?(88)?01[3-9]\d{8}$' #Returns: bool: True if the mobile number is valid, False otherwise.
    return validate_regex(number, mobile_regex)

def validate_usa_telephone_number(number): #Validates if the given string is a valid telephone number of USA.
    telephone_regex = r'^\+?1?\s?\(?\d{3}\)?[-\s]?\d{3}[-\s]?\d{4}$' #Returns: bool: True if the telephone number is valid, False otherwise.
    return validate_regex(number, telephone_regex)

def validate_password(password): #Validates if the given string is a valid password.
    if len(password) != 16:
        return False

    if not any(char.isupper() for char in password):
        return False

    if not any(char.islower() for char in password):
        return False

    if not any(char.isdigit() for char in password):
        return False

    special_characters = r'[@$!%*?&]'
    if not re.search(special_characters, password):
        return False

    return True

# Test the functions
email = "example@email.com"
print("Email:", validate_email(email))

mobile_number = "+8801712345678"
print("Bangladeshi Mobile Number:", validate_bangladeshi_mobile_number(mobile_number))

telephone_number = "+1 (123) 456-7890"
print("USA Telephone Number:", validate_usa_telephone_number(telephone_number))

password = "Abcdefg123@!$%^&"
print("Password:", validate_password(password))


