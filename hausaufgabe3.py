import hashlib

if hashlib.sha1('aaa'.encode('utf-8')).hexdigest() == "7e240de74fb1ed08fa08d38063f6a6a91462a815":
    print("Hell yeah")

woerterbuch = open('woerterbuch.txt', 'r')

for zeile in woerterbuch:
    if hashlib.sha1(zeile[:-1].encode('utf-8')).hexdigest() == "052a3c16072efa89c25f7ab9417794876fd2c131":
        print("Fuck ja: " + zeile)
print("fertig")