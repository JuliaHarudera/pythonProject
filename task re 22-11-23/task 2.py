import re


def validate_credit_card(card_number):
    pattern = re.compile(r'^\d{4}-\d{4}-\d{4}-\d{4}$')

    if re.match(pattern, card_number):
        return True
    else:
        return False


card_number = "1234-5678-9012-3456"
if validate_credit_card(card_number):
    print(f"Номер кредитной карты {card_number} действителен..")
else:
    print(f"Номер кредитной карты {card_number} не действителен..")
