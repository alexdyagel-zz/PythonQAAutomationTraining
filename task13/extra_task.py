import os
import sys
import logging

logger = logging.getLogger(__name__)
formatter = logging.Formatter('%(asctime)s - %(name)s : %(levelname)s - %(message)s')
screen_handler = logging.StreamHandler(sys.stdout)
screen_handler.setLevel(logging.DEBUG)
screen_handler.setFormatter(formatter)
logger.addHandler(screen_handler)
logger.setLevel(logging.DEBUG)


def check_parenthesis_consistency(file_name):
    if not os.path.isfile(file_name):
        raise NameError("File {} not found".format(file_name))

    logger.info("Filename to work with: {}".format(file_name))
    opening_bracket = tuple('({[<')
    closing_bracket = tuple(')}]>')
    bracket_pairs = dict(zip(opening_bracket, closing_bracket))
    queue_of_open_brackets = []

    with open(file_name, 'r') as source_file:
        for line_number, line in enumerate(source_file.readlines()):
            for offset, symbol in enumerate(line):
                if symbol in opening_bracket:
                    queue_of_open_brackets.append(symbol)
                elif symbol in closing_bracket and (not queue_of_open_brackets
                                                    or symbol != bracket_pairs[queue_of_open_brackets.pop()]):
                    logger.info("invalid syntax line: {} offset: {}".format(line_number + 1, offset + 1))
                    return False

    if queue_of_open_brackets:
        logger.info("invalid syntax: {} unclosed bracket(s)".format(len(queue_of_open_brackets)))
    else:
        logger.info("The code is correct")

    return not queue_of_open_brackets


if __name__ == '__main__':
    check_parenthesis_consistency("input_file1.txt")
