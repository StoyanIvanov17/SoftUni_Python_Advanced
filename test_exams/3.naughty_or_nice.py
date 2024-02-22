def naughty_or_nice_list(santa_list, *args, **kwargs):
    behaviour_list = {"Nice": [], "Naughty": []}

    for data in args:
        counting_numbers = [item[0] for item in santa_list]
        number, status = data.split('-')
        number = int(number)

        if counting_numbers.count(number) == 1:
            for kid_num, kid_name in santa_list:
                if kid_num == number:
                    behaviour_list[status].append(kid_name)
                    santa_list.remove((kid_num, kid_name))
                    break

    for name, value in kwargs.items():
        counting_names = [item[1] for item in santa_list]
        if counting_names.count(name) == 1:
            for kid_number, kid_name in santa_list:
                if name == kid_name:
                    behaviour_list[value].append(name)
                    santa_list.remove((kid_number, kid_name))
                    break

    behaviour_list["Not found"] = [x[1] for x in santa_list]

    result = ""

    for status, kids in behaviour_list.items():
        if kids:
            result += f"{status}: {', '.join(kids)}\n"

    return result

