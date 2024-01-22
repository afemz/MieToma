import time


class FULL_RESOLUTION:
    FULL = 200
    THREE_QUARTER = 150
    HALF = 100
    QUARTER = 50


class ONE_EIGHTH_RESOLUTION:
    FULL = 1600
    THREE_QUARTER = 1000
    HALF = 800
    QUARTER = 400


class ONE_SIXTEENTH_RESOLUTION:
    FULL = 3200
    THREE_QUARTER = 2400
    HALF = 1600
    QUARTER = 800


RESOLUTION_FULL_ONE_ROTATION = FULL_RESOLUTION.FULL
RESOLUTION_FULL_HALF_ROTATION = ONE_EIGHTH_RESOLUTION.HALF

# RESOLUTION_ONE_EIGHTH_ROTATION_FULL = ONE_EIGHTH_RESOLUTION.FULL

gpio_pin_CW_PLUS = 23
gpio_pin_CLK_PLUS = 21


def PUMP_KETCHUP_FULL_ROTATION():
    count_a = 0  # DEBUG PURPOSES
    count_b = 0  # DEBUG PURPOSES
    # GPIO.output(gpio_pin_CW_PLUS, GPIO.HIGH)
    # print("masuk sini")
    for i in range(RESOLUTION_FULL_ONE_ROTATION):  # DEFINES THE RESOLUTION
        print("task a executed " + str(count_a) + " number of times")
        count_a += 1
        time.sleep(0.01)
        # GPIO.output(gpio_pin_CLK_PLUS, GPIO.HIGH)
        print("task b executed " + str(count_b) + " number of times")
        count_b += 1
        time.sleep(0.01)
        # GPIO.output(gpio_pin_CLK_PLUS, GPIO.LOW)


def PUMP_KETCHUP_HALF():
    count_a = 0  # DEBUG PURPOSES
    count_b = 0  # DEBUG PURPOSES
    # GPIO.output(gpio_pin_CW_PLUS, GPIO.HIGH)
    print("masuk sini")
    for i in range(RESOLUTION_FULL_HALF_ROTATION):
        print("task a executed " + str(count_a) + " number of times")
        count_a += 1
        time.sleep(0.01)
        # GPIO.output(gpio_pin_CLK_PLUS, GPIO.HIGH)

        print("task b executed " + str(count_b) + " number of times")
        count_b += 1
        time.sleep(0.01)
        # GPIO.output(gpio_pin_CLK_PLUS, GPIO.LOW)
