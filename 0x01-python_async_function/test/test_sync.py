#!/usr/bin/env python3
#  asynchronous version ======================
# countasync.py
# https://realpython.com/async-io-python/

import asyncio

async def count():
    print("One")
    await asyncio.sleep(1)
    print("Two")

async def main():
    await asyncio.gather(count(), count(), count())

if __name__ == "__main__":
    import time
    s = time.perf_counter()

    # loop = asyncio.get_event_loop()
    # loop.run_until_complete(main())

    asyncio.run(main())
    elapsed = time.perf_counter() - s
    print(f"{__file__} executed in {elapsed:0.2f} seconds.")
