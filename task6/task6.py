import os


def truncate_file(file_name, lines):
    symbol_left = -1
    with open(file_name, 'rb') as source_file:
        if os.stat(file_name).st_size == 0:
            return ""
        source_file.seek(symbol_left, os.SEEK_END)
        lines_seen = 0
        while lines_seen < lines and source_file.tell() > 0:
            if source_file.read(1) == b'\n':
                lines_seen += 1
                if lines_seen == lines:
                    break
            source_file.seek(2 * symbol_left, os.SEEK_CUR)
        return source_file.read()


def create_file_by_truncating(file_name, lines=10):
    if not os.path.isfile(file_name):
        return
    truncated_lines = truncate_file(file_name, lines)
    directory = os.path.dirname(file_name)
    name = os.path.basename(file_name)
    with open(os.path.join(directory, 'truncated_' + name), 'wb') as new_file:
        new_file.write(truncated_lines)


if __name__ == '__main__':
    create_file_by_truncating("hello.txt")
