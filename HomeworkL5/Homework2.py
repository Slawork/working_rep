import re

def validate_phone_regex_only(text):
    match = re.search(r'\+?\d+', re.sub(r'[^\d+]', '', text))
    if match:
        number = match.group()
        if re.fullmatch(r'\+\d{10,12}', number):
            return number
    return "Ошибка: неверный формат номера"

print(validate_phone_regex_only("Телефон: +7 (912) 345-67-89"))