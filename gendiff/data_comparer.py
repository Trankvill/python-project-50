#!/usr/bin/env python


def compare_data(data1, data2):
    diff = '{'
    keys1, keys2 = set(data1.keys()), set(data2.keys())
    combained_keys = sorted(keys1 | keys2)
    for key in combained_keys:
        if key not in data1 and key in data2:
            diff += f'\n  + {key}: {str(data2[key]).lower()}'

        elif key in data1 and key not in data2:
            diff += f'\n  - {key}: {str(data1[key]).lower()}'

        elif data1[key] == data2[key]:
            diff += f'\n    {key}: {data2[key]}'

        elif isinstance(data1[key], dict) and isinstance(data2[key], dict):
            diff += f'\n  {key}: {compare_data(data1[key], data2[key])}'

        else:
            diff += f'\n  - {key}: {data1[key]}'
            diff += f'\n  + {key}: {data2[key]}'

    return diff + '\n}\n'
