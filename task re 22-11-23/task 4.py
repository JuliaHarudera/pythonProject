import re


def validate_login(login):
    pattern = re.compile(r'^[a-zA-Z0-9]{2,10}$')

    if re.match(pattern, login):
        return True
    else:
        return False


login_input = "user123"
if validate_login(login_input):
    print(f"Логин {login_input} действителен..")
else:
    print(f"Логин {login_input} не действителен..")
