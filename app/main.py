import re
import requests

# Пример базы данных лицензий (в реальном приложении это может быть база данных или API)
LICENSE_DATABASE = {
    "AAAA-BBBB-CCCC-DDDD": {"original": True, "expiry_date": "2024-12-31"},
    "EEEE-FFFF-GGGG-HHHH": {"original": False, "expiry_date": "2023-11-30"},
    # Добавьте другие лицензии по мере необходимости
}

def find_license_key(text):
    # Регулярное выражение для поиска ключа лицензии
    license_key_pattern = r"[A-Z0-9]{4}-[A-Z0-9]{4}-[A-Z0-9]{4}-[A-Z0-9]{4}"
    match = re.search(license_key_pattern, text)
    if match:
        return match.group(0)
    return None

def check_originality(license_key):
    # Проверка оригинальности лицензии
    if license_key in LICENSE_DATABASE:
        return LICENSE_DATABASE[license_key]["original"]
    return False

def get_expiry_date(license_key):
    # Извлечение срока действия лицензии
    if license_key in LICENSE_DATABASE:
        return LICENSE_DATABASE[license_key]["expiry_date"]
    return None

def main():
    # Пример текста, содержащего ключ лицензии
    text = "Your license key is AAAA-BBBB-CCCC-DDDD."

    # Найти ключ лицензии
    license_key = find_license_key(text)
    if license_key:
        print(f"Found license key: {license_key}")

        # Проверить оригинальность
        is_original = check_originality(license_key)
        if is_original:
            print("The software is original.")
        else:
            print("The software is not original.")

        # Извлечь срок действия лицензии
        expiry_date = get_expiry_date(license_key)
        if expiry_date:
            print(f"The license expires on: {expiry_date}")
        else:
            print("Expiry date not found.")
    else:
        print("License key not found.")

if __name__ == "__main__":
    main()
