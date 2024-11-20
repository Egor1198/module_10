import datetime
import multiprocessing


def read_info(name):
    all_data = []
    with open(name) as file:
        while True:
            line = file.readline()
            all_data.append(line)
            if not line:
                break


filenames = [f'./file {number}.txt' for number in range(1, 5)]


start_1 = datetime.datetime.now()
for file in filenames:
    read_info(file)
end_1 = datetime.datetime.now()
print(f'{end_1 - start_1} (линейный)')


if __name__ == '__main__':
    start_2 = datetime.datetime.now()
    with multiprocessing.Pool(processes=len(filenames)) as pool:
        pool.map(read_info, filenames)
    end_2 = datetime.datetime.now()
    print(f'{end_2 - start_1} (многопроцессорный)')
