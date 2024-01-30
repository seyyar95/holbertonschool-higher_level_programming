#!/usr/bin/python3
def roman_to_int(roman_string):
    if roman_string is None or not isinstance(roman_string, str):
        return 0
    rom_dic = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
    num = 0
    """
    this one also works

    for i in range(len(roman_string)):
        if i > 0 and rom_dic[roman_string[i]] > rom_dic[roman_string[i - 1]]:
            num = num + rom_dic[roman_string[i]] - 2
            # * rom_dic[roman_string[i - 1]]
        else:
            num = num + rom_dic[roman_string[i]]

       but we have this too
    """
    element = 0
    for i in reversed(roman_string):
        val = rom_dic[i]
        if val >= element:
            num = num + val
        else:
            num = num - val
        element = val
    return num
