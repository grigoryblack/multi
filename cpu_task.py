import concurrent.futures
import timeit
from hashlib import md5
from random import choice


def mining(worker_id):
    start_time = timeit.default_timer()
    search_time = 0
    while True:
        s = "".join([choice("0123456789") for _ in range(50)])
        h = md5(s.encode('utf8')).hexdigest()

        if h.endswith("00000"):
            print(s, h)
            search_time = timeit.default_timer() - start_time - search_time
            print(f'{worker_id} процессор: найдена монета за {search_time} секунд\n')


def start():
    max_workers = 7
    with concurrent.futures.ProcessPoolExecutor(max_workers=max_workers) as executor:
        for i in range(1, max_workers + 1):
            executor.submit(mining, i)


if __name__ == '__main__':
    start()
