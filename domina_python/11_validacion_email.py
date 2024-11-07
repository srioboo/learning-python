import re


def email_valido(email):
    formato_valid = r"^([a-z0-9]+[-_.])*[a-z0-9]+@[a-z0-9]+(\.[a-z]{2,})+$"
    if re.match(formato_valid, email, re.IGNORECASE):
        return True
    return False

valido = email_valido("salva@gmail.com")
print("Email valido:", valido)