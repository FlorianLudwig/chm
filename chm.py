import sys
import time
import collections

import requests


def main():
    frequency = 0.5
    request_timeout = 0.5
    code = collections.Counter()
    while True:
        t = time.time()
        try:
            response = requests.get(sys.argv[1], timeout=request_timeout)
            code[response.status_code] += 1
        except requests.exceptions.ConnectionError:
            code['ConnectionError'] += 1
        except requests.exceptions.ReadTimeout:
            code['timeout'] += 1
        print(code)
        diff = time.time() -t
        if diff < frequency:
            time.sleep(frequency - diff)


if __name__ == '__main__':
    try:
        main()
    except KeyboardInterrupt:
        pass
