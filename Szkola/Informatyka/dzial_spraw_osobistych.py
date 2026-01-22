operations_num = int(input("Podaj liczbe operacji:"))
database = {}

for i in range(operations_num):
    operation = input("Podaj operacje")
    parts = operation.split()

    match parts[0]:
        case '+':
            name = parts[1] + " " + parts[2]
            database[name] = 0
        case '!':
            amount = parts[3]
            name = parts[1] + " " + parts[2]
            database[name] += int(amount)
        case '/':
            name = parts[1] + " " + parts[2]
            new_name = parts[3] + " " + parts[4]
            amount = database[name]
            database.pop(name)
            database[new_name] = amount

sorted_keys= sorted([i for i in database])

for key in sorted_keys:
    print('\n', key, database[key])