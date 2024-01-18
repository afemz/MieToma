import PUMP_RESOLUTION_ROTATION as PR
import PUMP_ROTATION as PRo
import time
import RPi._GPIO as GPIO

RESOLUTION_FULL_ROTATION_FULL = PR.FULL_RESOLUTION.FULL  # FULL RESOLUTION FULL ROTATION
RESOLUTION_FULL_ROTATION_THREE_QUARTER = (
    PR.FULL_RESOLUTION.THREE_QUARTER
)  # FULL RESOLUTION THREE QUARTER REVOLUTION
RESOLUTION_FULL_ROTATION_QUARTER = (
    PR.FULL_RESOLUTION.QUARTER
)  # FULL RESOLUTION QUARTER REVOLUTION
RESOLUTION_FULL_ROTATION_HALF = (
    PR.FULL_RESOLUTION.HALF
)  # FULL RESOLUTION HALF REVOLUTION


RESOLUTION_ONE_EIGHTH_ROTATION_FULL = PR.ONE_EIGHTH_RESOLUTION.FULL

gpio_pin_CW_PLUS = 23
gpio_pin_CLK_PLUS = 21


def PUMP_KETCHUP_FULL_ROTATION():
    count_a = 0  # DEBUG PURPOSES
    count_b = 0  # DEBUG PURPOSES
    GPIO.output(gpio_pin_CW_PLUS, GPIO.HIGH)
    # print("masuk sini")
    for i in range(RESOLUTION_FULL_ROTATION_FULL):  # DEFINES THE RESOLUTION
        print("task a executed " + str(count_a) + " number of times")
        count_a += 1
        time.sleep(0.01)
        GPIO.output(gpio_pin_CLK_PLUS, GPIO.HIGH)
        print("task b executed " + str(count_b) + " number of times")
        count_b += 1
        time.sleep(0.01)
        GPIO.output(gpio_pin_CLK_PLUS, GPIO.LOW)


def PUMP_KETCHUP_HALF():
    count_a = 0  # DEBUG PURPOSES
    count_b = 0  # DEBUG PURPOSES
    GPIO.output(gpio_pin_CW_PLUS, GPIO.HIGH)
    print("masuk sini")
    for i in range(RESOLUTION_FULL_ROTATION_HALF):
        print("task a executed " + str(count_a) + " number of times")
        count_a += 1
        time.sleep(0.01)
        GPIO.output(gpio_pin_CLK_PLUS, GPIO.HIGH)

        print("task b executed " + str(count_b) + " number of times")
        count_b += 1
        time.sleep(0.01)
        GPIO.output(gpio_pin_CLK_PLUS, GPIO.LOW)
