import re


def validate_email(email):
    pattern = re.compile(r'^[a-zA-Z0-9]+([._-]?[a-zA-Z0-9]+)*@[a-zA-Z0-9]+([.-]?[a-zA-Z0-9]+)*\.[a-zA-Z]{2,}$')

    # Перевірте, чи введена електронна пошта відповідає шаблону
    if re.match(pattern, email):
        return True
    else:
        return False


email_address = "user_name123@example-mail.com"
if validate_email(email_address):
    print(f"Адрес электронной почты {email_address} действителен..")
else:
    print(f"Адрес электронной почты {email_address} не действителен..")