import PUMP_RESOLUTION_ROTATION as PR
import PUMP_ROTATION as PRo
import time

RESOLUTION_FULL_ROTATION_FULL = PR.FULL_RESOLUTION.FULL
RESOLUTION_FULL_ROTATION_THREE_QUARTER = PR.FULL_RESOLUTION.THREE_QUARTER
RESOLUTION_FULL_ROTATION_QUARTER = PR.FULL_RESOLUTION.QUARTER
RESOLUTION_FULL_ROTATION_HALF = PR.FULL_RESOLUTION.HALF


RESOLUTION_ONE_EIGHTH_ROTATION_FULL = PR.ONE_EIGHTH_RESOLUTION.FULL


def PUMP_KETCHUP_FULL_ROTATION():
    # do something
    # maybe delay smth``
    count_rotation = 0
    count_rotation += 1
    count_a = 0
    count_b = 0
    # print("masuk sini")
    for i in range(RESOLUTION_FULL_ROTATION_FULL):  # DEFINES THE RESOLUTION
        print("task a executed " + str(count_a) + " number of times")
        count_a += 1
        time.sleep(0.01)
        print("task b executed " + str(count_b) + " number of times")
        count_b += 1
        time.sleep(0.01)


def PUMP_KETCHUP_HALF():
    # do something
    # maybe delay smth
    count_a = 0
    count_b = 0
    print("masuk sini")
    for i in range(RESOLUTION_FULL_ROTATION_HALF):
        print("task a executed " + str(count_a) + " number of times")
        count_a += 1
        time.sleep(0.01)

        print("task b executed " + str(count_b) + " number of times")
        count_b += 1
        time.sleep(0.01)
