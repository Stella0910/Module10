import time
import datetime
import multiprocessing


def read_info(name):
    all_data = []
    with open(name) as file:
        for line in file:
            all_data += line


filenames = [f'./file {number}.txt' for number in range(1, 5)]

# start_time = time.time()
# read_info('file 1.txt')
# read_info('file 2.txt')
# read_info('file 3.txt')
# read_info('file 4.txt')
# end_time = time.time()
# print(datetime.timedelta(seconds=end_time - start_time))


if __name__ == '__main__':
    start_time = time.time()
    with multiprocessing.Pool() as p:
        p.map(read_info, filenames)
    end_time = time.time()
    print(datetime.timedelta(seconds=end_time - start_time))
