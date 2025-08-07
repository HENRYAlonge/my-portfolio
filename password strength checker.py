#Password checker
print("Enter a password")
password = input("")
is_long_enough = len(password) >= 8
has_digit = False
has_uppercase = False
has_special = False

for char in password:
    if char.isdigit():
        has_digit = True
    if char.isupper():
            has_uppercase = True
    if  not char.isalnum():
        has_special = True

if is_long_enough and has_digit and has_uppercase and has_special:
    print("Password is strong")
else:
    print("Password is weak")