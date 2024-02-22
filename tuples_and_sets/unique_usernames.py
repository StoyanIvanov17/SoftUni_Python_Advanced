usernames_count = int(input())

unique_usernames = set()
for i in range(usernames_count):
    name = input()
    unique_usernames.add(name)

for name in unique_usernames:
    print(name)