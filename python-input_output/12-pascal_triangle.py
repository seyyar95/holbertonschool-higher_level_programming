#!/usr/bin/python3
"""Module Doc"""


def pascal_triangle(n):
    """Pascal Triangle"""
    if n <= 0:
        return []

    new_list = []

    for i in range(n):
        if i == 0:
            row = []
            row.append(1)
            new_list.append(row)
        elif i > 0:
            row = []
            for j in range(i + 1):
                if j == 0:
                    row.append(1)
                elif j == i:
                    row.append(1)
                elif i == 2:
                    row.append(j + row[j - 1])
                else:
                    row.append(new_list[i-1][j-1] + new_list[i-1][j])
            new_list.append(row)
    return new_list
