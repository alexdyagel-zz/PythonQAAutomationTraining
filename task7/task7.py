from datetime import datetime
import time
import sys


def print_time_with_delay(delay=60, attempts_to_exit=3):
    while True:
        try:
            time.sleep(delay)
            print(datetime.now().strftime('%H:%M:%S'))
        except KeyboardInterrupt:
            attempts_to_exit -= 1
            print("Attempts left: {}".format(attempts_to_exit))
            if attempts_to_exit == 0:
                print("Are you sure you want to exit? (y/n)")
                reply = input()
                if reply.lower() == 'y':
                    print("Exiting...")
                    break
                else:
                    attempts_to_exit += 1


def is_int(string):
    try:
        int(string)
    except ValueError:
        return False
    return True


if __name__ == '__main__':
    try:

        if len(sys.argv) < 1 or len(sys.argv) > 3:
            raise ValueError("You should pass 0, 1 or 2 arguments in script."
                             " Number of passed arguments {}".format(len(sys.argv) - 1))

        if len(sys.argv) >= 2:
            if not is_int(sys.argv[1]):
                raise ValueError("Argument(s) should be convertable to integer numbers.")
            sys.argv[1] = int(sys.argv[1])

        if len(sys.argv) == 3:
            if not is_int(sys.argv[2]):
                raise ValueError("Argument(s) should be convertable to integer numbers.")
            sys.argv[2] = int(sys.argv[2])

        print_time_with_delay(*sys.argv[1:])

    except ValueError as err:
        print("ValueError: {}".format(err))
