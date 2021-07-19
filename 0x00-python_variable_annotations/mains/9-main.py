#!/usr/bin/env python3
import sys


if __name__ == '__main__':
    sys.path.append('..')

    element_length =  __import__('9-element_length').element_length

    print(element_length.__annotations__)
