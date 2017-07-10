def front_back(str):
    if len(str) <= 1:
        return str

    first_c = str[0]
    last_c = str[-1]
    middle = str[1:-1]
    return (last_c + middle + first_c)