from itertools import product
from string import ascii_lowercase
from concurrent.futures import ThreadPoolExecutor
import hashlib
import time


hashes = [
    '1115dd800feaacefdf481f1f9070374a2a81e27880f187396db67958b207cbad',
    '3a7bd3e2360a3d29eea436fcfb7e44c735d117c42d1c1835420b6b9942dd4f1b',
    '74e1bb62f8dabb8125a58852b63bdf6eaef667cb56ac7f7cdba6d7305c50a22f',
    '7a68f09bd992671bb3b19a5e70b7827e']


passwords = [''.join(seq) for seq in product(ascii_lowercase, repeat=5)]


def brute_force(hash_values):
    start_time = time.time()
    d = {}
    for password in passwords:

        if len(d) == 4:
            t = round(time.time() - start_time, 2)
            return d, t

        md5_hash = hashlib.md5(password.encode()).hexdigest()
        if md5_hash in hash_values:
            d[password] = md5_hash
            continue


        sha256_hash = hashlib.sha256(password.encode()).hexdigest()
        if sha256_hash in hash_values:
            d[password] = sha256_hash
            continue

def brute_force_multi(hash_values, num_threads):
    with ThreadPoolExecutor(max_workers=num_threads) as executor:
        futures = executor.submit(brute_force, hash_values)
        results = futures.result()
        return results



program_type = input('Ввведите single для однопоточного зупуска, multi - многопоточного: ')
if program_type not in ('single', 'multi'):
    print('Выбран неверный режим запуска')
    exit()

if program_type == 'single':
    d, t = brute_force(hashes)
    print(f'Время перебора паролей: {t} секунд')
    for password, hash_value in d.items():
        print(f'{password = }: hash = {hash_value}')

else:
    try:
        num_threads = int(input('Введите количество потоков от 1 до 16: '))
        if num_threads not in [i for i in range(1, 17)]:
            print('Неверный ввод')
            exit()
    except Exception as e:
        print('Неверный ввод')
        exit()


    d, t = brute_force_multi(hashes, num_threads)
    print(f'Время перебора паролей: {t} секунд')
    for password, hash_value in d.items():
        print(f'{password = }: hash = {hash_value}')








