#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import os
import threading
import time
import sys
import logging
from functools import wraps

logger = logging.getLogger(__name__)
logfile = "script_log.log"
span_time = 2
run_tracker = []

formatter = logging.Formatter('%(asctime)s - %(name)s : %(threadName)s - %(levelname)s - %(message)s')
screen_handler = logging.StreamHandler(sys.stdout)
screen_handler.setLevel(logging.DEBUG)
screen_handler.setFormatter(formatter)

file_handler = logging.FileHandler(logfile)
file_handler.setLevel(logging.INFO)
file_handler.setFormatter(formatter)

logger.addHandler(screen_handler)
logger.addHandler(file_handler)
logger.setLevel(logging.DEBUG)

start_time = time.time()


def threaded_execution(func):
    @wraps(func)
    def func_wrapper(*args):
        thread = threading.Thread(target=func, args=args)
        thread.start()

    return func_wrapper


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


@threaded_execution
def create_file_by_truncating(file_name, lines=10):
    logger.info("Filename to work with: {}".format(file_name))
    run_tracker.append(file_name)
    time.sleep(span_time)
    if not os.path.isfile(file_name):
        raise FileNotFoundError
    truncated_lines = truncate_file(file_name, lines)
    directory = os.path.dirname(file_name)
    name = os.path.basename(file_name)
    with open(os.path.join(directory, 'truncated_' + name), 'wb') as new_file:
        new_file.write(truncated_lines)


if __name__ == "__main__":
    logger.info("Starting a chain of long functions")
    create_file_by_truncating("input_file1.txt", 5)
    create_file_by_truncating("input_file2.txt", 6)

    logger.info("Starting long main logic")
    time.sleep(span_time)
    ########################
    # --- Summary part --- #
    ########################
    total_time = time.time() - start_time
    logger.info("The run took '{:.3}' seconds".format(total_time))
    assert len(run_tracker)  # Do NOT remove or change, we need to ensure long_long_function ever ran
    assert total_time < (span_time + 1)  # +1 second is granted for all the threads to get allocated
