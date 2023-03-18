#-------------------------------------------------------------------------------
# Name:        module1
# Purpose:
#
# Author:      S K Digital
#
# Created:     18/03/2023
# Copyright:   (c) S K Digital 2023
# Licence:     <your licence>
#-------------------------------------------------------------------------------

import random
import math

data="0123456789abcyheidnfrfhrfyghryghrhy4u"

leng = len(data)

otp=""

for i in range(6):
    otp += data[math.floor(random.random()*leng)]

print("your otp is",otp)