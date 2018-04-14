import sys
import time
import collections

import requests


def main():
    code = collections.Counter()
    while True:
        t = time.time()
        try:
            response = requests.get(sys.argv[1])
            code[response.status_code] += 1
        except requests.exceptions.ConnectionError:
            code['ConnectionError'] += 1
        print(code)
        diff = time.time() -t
        if diff < 1:
            time.sleep(1 - diff)


if __name__ == '__main__':
    try:
        main()
    except KeyboardInterrupt:
        pass
