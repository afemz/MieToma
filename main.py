import time
import sys

path = "D:\Side Project\mietoma\Py\LIBRARY"  # Determine system path

sys.path.append(path)

from LIBRARY.PUMP_KETCHUP import PUMP_KETCHUP_FULL_ROTATION  # Buat manggil fungsi
from LIBRARY.PUMP_RESOLUTION_ROTATION import FULL_RESOLUTION  # Buat manggil class

PUMP_KETCHUP_FULL_ROTATION()

"""
# Buat declare class
FR = FULL_RESOLUTION()
full_res = FR.FULL
print(full_res)

"""
