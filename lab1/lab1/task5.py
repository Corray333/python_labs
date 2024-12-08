import re

def find_dates(string):
    # Шаблон для поиска дат в нужном формате
    pattern = r'\b\d{1,2} (?:января|февраля|марта|апреля|мая|июня|июля|августа|сентября|октября|ноября|декабря) \d{4}\b'
    dates = re.findall(pattern, string)
    return dates

# Пример строки
string = "События происходили 22 февраля 2022, а также 24 февраля 2022 и 21 марта 2014."

# Поиск всех дат
found_dates = find_dates(string)
print("Найденные даты:", found_dates)
