#!/usr/bin/env python3
import sys
import asyncio

if __name__ == '__main__':
    sys.path.append('..')

    task_wait_n = __import__('4-tasks').task_wait_n

    n = 5
    max_delay = 6
    print(asyncio.run(task_wait_n(n, max_delay)))
