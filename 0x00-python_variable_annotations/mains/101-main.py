#!/usr/bin/env python3
import sys


if __name__ == '__main__':
    sys.path.append('..')
    safely_get_value = __import__('101-safely_get_value').safely_get_value
    annotations = safely_get_value.__annotations__
    print("Here's what the mappings should look like")
    for k, v in annotations.items():
        print( ("{}: {}".format(k, v)))
