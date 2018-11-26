To make the code below work, create a parametrized decorator named “caching”.

Store it in a separate module named “functional_utils”.

Let it accept timeout as an argument for return values retention.


 -*- coding: utf-8 -*-
import random
import time

 

from functional import caching

=== here be your code ===
 === do not modify below ===
SLEEP_SPAN = 3


def _users_slow_selector():
    time.sleep(SLEEP_SPAN // 2)
    return random.randint(0x5000, 0x10000)


@caching(timeout=SLEEP_SPAN)
def get_driver_id():
    return _users_slow_selector()


@caching(timeout=SLEEP_SPAN)
def get_passenger_id():
    return _users_slow_selector()


driver1 = get_driver_id()
passenger1 = get_passenger_id()

driver2 = get_driver_id()
passenger2 = get_passenger_id()

assert driver1 is driver2, "Drivers differ, but should be same!"
assert passenger1 is passenger2, "Passengers differ, but should be same!"

=== Exhaust the caching timer ====
time.sleep(SLEEP_SPAN)

driver3 = get_driver_id()
passenger3 = get_passenger_id()

assert driver2 is not driver3, "Drivers are same, but cache should have been expired and you get a new one!"
assert passenger2 is not passenger3, "passengers are same, but cache should have been expired and you get a new one!"

 
