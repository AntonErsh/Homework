from datetime import datetime
from multiprocessing import Pool


def read_info(name: str):
    all_data = []
    with open(name, encoding='utf-8') as file_txt:
        while True:
            line = file_txt.readline()
            all_data.append(line)
            if not line:
                break


list_files = ['file 1.txt', 'file 2.txt', 'file 3.txt', 'file 4.txt']
# time_start = datetime.now()
# for file in list_files:
#     read_info(file)
# time_end = datetime.now()
# print(time_end - time_start)
if __name__ == '__main__':
    time_start = datetime.now()
    with Pool(processes=len(list_files)) as pool:
        pool.map(read_info, list_files)
    time_end = datetime.now()
    print(time_end - time_start)
