#!/usr/bin/env python3
'''
Test file for printing the correct output of the wait_n coroutine
'''
import sys
import asyncio

if __name__ == '__main__':
    sys.path.append('..')
    wait_n = __import__('1-concurrent_coroutines').wait_n

    print(asyncio.run(wait_n(5, 5)))
    print(asyncio.run(wait_n(10, 7)))
    print(asyncio.run(wait_n(10, 0)))
