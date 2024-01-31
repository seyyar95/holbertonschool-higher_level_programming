#!/usr/bin/python3
def roman_to_int(roman_string):
    if roman_string is None or isinstance(roman_string, int):
        return 0

    num = 0

    for i in range(len(roman_string)):
        if i > 0 and rom_dic[roman_string[i]] > rom_dic[roman_string[i - 1]]:
            num = num + rom_dic[roman_string[i]] - 2
        else:
            num = num + rom_dic[roman_string[i]]
    return num
