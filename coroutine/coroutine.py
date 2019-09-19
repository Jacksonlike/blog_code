import requests
import time
import threading
from multiprocessing import Process
from functools import wraps
import asyncio
import aiohttp


def func_time(func):
    @wraps(func)
    def new_func(*args, **kwargs):
        print(f'start {func.__name__}')
        start  = time.time()
        result = func(*args, **kwargs)
        stop   = time.time()
        print(f'finish {func.__name__}, and taking {format(stop - start, "0.2f")} s')
        return result
    return new_func


def do_work(url):
    requests.get(url)


@func_time
def do_works_serial(tasks):
    for task in tasks:
        do_work(task)


@func_time
def do_works_muti_threads(tasks):
    threads = set()
    for task in tasks:
        t = threading.Thread(target=do_work, args=(task,))
        t.start()
        threads.add(t)

    # 等待所有线程的结束
    for t in threads:
        t.join()


@func_time
def do_works_muti_processes(tasks):
    processes = set()
    for task in tasks:
        t = Process(target=do_work, args=(task,))
        t.start()
        processes.add(t)

    # 等待所有进程的结束
    for t in processes:
        t.join()


async def do_work_async(url):
    print(f'{url}:{threading.currentThread().ident}')
    async with aiohttp.ClientSession() as session:
        async with session.get(url) as _:
            print(f'{url} done')


async def coro_func(tasks):
    tasks = (asyncio.create_task(do_work_async(task)) for task in tasks)
    print('before tasks')
    await asyncio.gather(*tasks)
    print('finish tasks')


@func_time
def do_works_coroutine(tasks):
    asyncio.run(coro_func(tasks))


def main():
    tasks = [
        "https://movie.douban.com/subject/5912992/",
        "https://movie.douban.com/subject/30170448/",
        "https://movie.douban.com/subject/30334073/",
        "https://movie.douban.com/subject/1292064/",
        "https://movie.douban.com/subject/21937445/",
    ]

    do_works_serial(tasks)
    do_works_muti_threads(tasks)
    do_works_muti_processes(tasks)
    do_works_coroutine(tasks)
    

if __name__ == '__main__':
    main()
