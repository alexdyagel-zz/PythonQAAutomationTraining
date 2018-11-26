import os


def get_files_from_os_walk(func, min_size_kb=0):
    bytes_in_kilobyte = 1024
    for folder, subs, files in func:
        for file_name in files:
            path = os.path.join(folder, file_name)
            if os.path.getsize(path) >= min_size_kb * bytes_in_kilobyte:
                yield unicode(path, 'cp1251')


if __name__ == '__main__':
    files_lister = get_files_from_os_walk(os.walk("d:\\automation python"))
    for i in files_lister:
        print i
