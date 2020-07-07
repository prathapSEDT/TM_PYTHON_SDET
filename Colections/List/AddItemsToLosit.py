data="?><(??)*&^%#$!"

symbols=list()

for sym in data:
    symbols.append(sym)

print(symbols)

lsit2=["k","o","p"]

symbols.extend(lsit2)
print(symbols)
print("----------------------------------")
symbols.reverse()
symbols.sort()
print(symbols)

print(symbols.count("?"))