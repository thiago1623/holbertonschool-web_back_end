#!/usr/bin/env python3

import sys
import asyncio

if __name__ == '__main__':
    sys.path.append('..')
    wait_random = __import__('0-basic_async_syntax').wait_random

    print(asyncio.run(wait_random()))
    print(asyncio.run(wait_random(5)))
    print(asyncio.run(wait_random(15)))
