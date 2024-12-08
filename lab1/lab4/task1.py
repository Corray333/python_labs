import re

def is_valid_ipv4(ip):
    pattern = re.compile(r'^(\d{1,3}\.){3}\d{1,3}$')
    if pattern.match(ip):
        parts = ip.split('.')
        for part in parts:
            if int(part) < 0 or int(part) > 255:
                return False
        return True
    return False

def validate_ipv4(ip):
    if not is_valid_ipv4(ip):
        raise ValueError("Некорректный IPv4 адрес")
    return ip

print(is_valid_ipv4("192.168.1.1")) 
print(is_valid_ipv4("256.256.256.256"))
print(validate_ipv4("192.168.1.1"))
print(validate_ipv4("256.256.256.256")) 