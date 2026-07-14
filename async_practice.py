#Without using async.io
import time 
import asyncio
import random

def count():
    print("One")
    time.sleep(1)
    print("Two")
    time.sleep(1)

def main():
    for _ in range(3):
        count()

if __name__ == "__main__":
    start = time.perf_counter()
    main()
    elapsed = time.perf_counter() - start
    print(f"{__file__} executed in {elapsed: 0.2f} seconds")

#using async.io

async def count():
    print("One")
    await asyncio.sleep(1)
    print("Two")
    await asyncio.sleep(1)

async def main():
    await asyncio.gather(count(), count(), count()) #to run 3 instances of count() concurrently

if __name__ == "__main__":
    import time

    start = time.perf_counter()
    asyncio.run(main())
    elapsed = time.perf_counter() - start
    print(f"{__file__} executed in {elapsed: 0.2f} seconds")    


#async def g():
    #result = await f() #pause and come back to g() when f() returns
    #return result #when Python encounters an await f() expression in the scope of a g() coroutine, await tells the event loop: suspend the execution of g() until the result of f() is returned. In the meantime, let something else run.


#async def f(x):
     #y = await z(x) #okay - await and return allowed in coriutines
     #return y 

#async def g(x):
    #yield x #okay - this is an async generator  

#async def m(x):
    #yield from gen(x) #syntax error 

#def n(x):
    #y = await z(x) #No syntax error (no async def here)
    #return y 

import asyncio
import random

COLORS = (
    "\033[0m",      # Reset
    "\033[36m",     # Cyan
    "\033[91m",     # Red
    "\033[35m"      # Magenta
)

async def main():
    return await asyncio.gather(
        makerandom(1, 9),
        makerandom(2, 8),
        makerandom(3, 8),
    )

async def makerandom(delay, threshold=6):
    color = COLORS[delay]
    print(f"{color}Initiated makerandom({delay}).")

    while (number := random.randint(0, 10)) <= threshold:
        print(f"{color}makerandom({delay}) == {number} too low; retrying.")
        await asyncio.sleep(delay)

    print(f"{color}----> Finished: makerandom({delay}) == {number}{COLORS[0]}")
    return number

if __name__ == "__main__":
    random.seed(444)
    r1, r2, r3 = asyncio.run(main())

    print()
    print(f"r1: {r1}, r2: {r2}, r3: {r3}")

async def main():
    print("Hello....")
    await asyncio.sleep(1)
    print("World")

routine = main()
routine
asyncio.run(routine)

import asyncio
import random
import time

async def main():
    user_ids = [1, 2, 3]
    start = time.perf_counter()
    await asyncio.gather(
        *(get_user_with_posts(user_id) for user_id in user_ids)
    )
    end = time.perf_counter()
    print(f"\n==> Total time: {end - start:.2f} seconds")

async def get_user_with_posts(user_id):
    user = await fetch_user(user_id)
    await fetch_posts(user)

async def fetch_user(user_id):
    delay = random.uniform(0.5, 2.0)
    print(f"User coro: fetching user by {user_id=}...")
    await asyncio.sleep(delay)
    user = {"id": user_id, "name": f"User{user_id}"}
    print(f"User coro: fetched user with {user_id=} (done in {delay:.1f}s).")
    return user

async def fetch_posts(user):
    delay = random.uniform(0.5, 2.0)
    print(f"Post coro: retrieving posts for {user['name']}...")
    await asyncio.sleep(delay)
    posts = [f"Post {i} by {user['name']}" for i in range(1, 3)]
    print(
        f"Post coro: got {len(posts)} posts by {user['name']}"
        f" (done in {delay:.1f}s):"
    )
    for post in posts:
        print(f" - {post}")

if __name__ == "__main__":
    random.seed(444)
    asyncio.run(main())

#queue based version posts to user


async def main():
    queue = asyncio.Queue()
    user_ids = [1, 2, 3]

    start = time.perf_counter()
    await asyncio.gather(
        producer(queue, user_ids),
        *(consumer(queue) for _ in user_ids),
    )
    end = time.perf_counter()
    print(f"\n==> Total time: {end - start:.2f} seconds")

async def producer(queue, user_ids):
    async def fetch_user(user_id):
        delay = random.uniform(0.5, 2.0)
        print(f"Producer: fetching user by {user_id=}...")
        await asyncio.sleep(delay)
        user = {"id": user_id, "name": f"User{user_id}"}
        print(f"Producer: fetched user with {user_id=} (done in {delay:.1f}s)")
        await queue.put(user)

    await asyncio.gather(*(fetch_user(uid) for uid in user_ids))
    for _ in range(len(user_ids)):
        await queue.put(None)  # Sentinels for consumers to terminate

async def consumer(queue):
    while True:
        user = await queue.get()
        if user is None:
            break
        delay = random.uniform(0.5, 2.0)
        print(f"Consumer: retrieving posts for {user['name']}...")
        await asyncio.sleep(delay)
        posts = [f"Post {i} by {user['name']}" for i in range(1, 3)]
        print(
            f"Consumer: got {len(posts)} posts by {user['name']}"
            f" (done in {delay:.1f}s):"
        )
        for post in posts:
            print(f"  - {post}")

if __name__ == "__main__":
    random.seed(444)
    asyncio.run(main())

import aiohttp


async def check(url):
    async with aiohttp.ClientSession() as session:
        async with session.get(url) as response:
            print(f"{url}: Status -> {response.status}")


async def main():
    websites = [
        "https://realpython.com",
        "https://pycoders.com",
        "https://www.python.org",
    ]

    await asyncio.gather(*(check(url) for url in websites))


asyncio.run(main())

import asyncio


async def coro(numbers):
    await asyncio.sleep(min(numbers))
    return list(reversed(numbers))


async def main():
    task = asyncio.create_task(coro([3, 2, 1]))

    print(f"{type(task) = }")
    print(f"{task.done() = }")

    return await task


result = asyncio.run(main())
print(f"result: {result}")

import asyncio
import time


async def coro(numbers):
    await asyncio.sleep(min(numbers))
    return list(reversed(numbers))


async def main():
    task1 = asyncio.create_task(coro([10, 5, 2]))
    task2 = asyncio.create_task(coro([3, 2, 1]))

    print("Start:", time.strftime("%X"))

    result = await asyncio.gather(task1, task2) #The gather() function is meant to neatly put a collection of coroutines into a single future object. 

    print("End:", time.strftime("%X"))
    print(f"Both tasks done: {all((task1.done(), task2.done()))}")

    return result


result = asyncio.run(main())
print(f"result: {result}")

import asyncio
import time


async def coro(numbers):
    await asyncio.sleep(min(numbers))
    return list(reversed(numbers))


async def main():
    task1 = asyncio.create_task(coro([10, 5, 2]))
    task2 = asyncio.create_task(coro([3, 2, 1]))

    print("Start:", time.strftime("%X"))

    for task in asyncio.as_completed([task1, task2]):
        result = await task
        print(f"Result: {result} completed at {time.strftime('%X')}")

    print("End:", time.strftime("%X"))
    print(f"Both tasks done: {all((task1.done(), task2.done()))}")


asyncio.run(main())

import asyncio


async def coro_a():
    await asyncio.sleep(1)
    raise ValueError("Error in coro A")


async def coro_b():
    await asyncio.sleep(2)
    raise TypeError("Error in coro B")


async def coro_c():
    await asyncio.sleep(0.5)
    raise IndexError("Error in coro C")


async def main():
    results = await asyncio.gather(
        coro_a(),
        coro_b(),
        coro_c(),
        return_exceptions=True
    )

    exceptions = [e for e in results if isinstance(e, Exception)]

    if exceptions:
        raise ExceptionGroup("Errors", exceptions)


asyncio.run(main())

try:
    asyncio.run(main())

except* ValueError as ve_group:
    print(f"[ValueError handled] {ve_group.exceptions}")

except* TypeError as te_group:
    print(f"[TypeError handled] {te_group.exceptions}")

except* IndexError as ie_group:
    print(f"[IndexError handled] {ie_group.exceptions}")


    

