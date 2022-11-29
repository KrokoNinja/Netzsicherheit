import hashlib

def md5(password, constant):
    m = hashlib.md5()
    m.update(str.encode(password + constant))
    return m.hexdigest()


def hashi(password, constant):
    if len(password) < 14:
        while len(password) < 14:
            password += "0"
    elif len(password) > 14:
        password = password[:14]
    first = password[:7]
    second = password[7:]
    firsthash = md5(first, constant)
    secondhash = md5(second, constant)
    return (firsthash + secondhash)[:32]

print(hashi("22334455", "NetSec1"))
