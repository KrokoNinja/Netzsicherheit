hashes_jan = open('Janhashes.txt', 'r')
hashes_yannik = open("Yannikhashes.txt", 'r')

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

for jan in hashes_jan:
    if hashi(jan, "NetSec1") == "a65dc44b9be4a73dda498b1fe098c2c3":
        print("Alright: " + jan)
print("Jan fertig!")


for yannik in hashes_yannik:
    if hashi(yannik[:-1], "NetSec1") == "dc8e9d697b7750cb4c7c2b258ef8fed4":
        print("Alright: " + yannik)
print("Yannik fertig!")