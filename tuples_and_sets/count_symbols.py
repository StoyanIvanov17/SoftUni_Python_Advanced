symbols_counter = {}

for letter in input():
    symbols_counter[letter] = symbols_counter.get(letter, 0) + 1

for keys, values in sorted(symbols_counter.items()):
    print(f"{keys}: {values} time/s")
