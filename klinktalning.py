#!/usr/bin/env python
# -*- encoding: UTF-8 -*-
WEIGHT_100 = 8.5
WEIGHT_50 = 8.25
WEIGHT_10 = 6.9
WEIGHT_5 = 6.5
WEIGHT_1 = 4.5

WELCOME_MESSAGE = u""
IN_MESSAGE_100 = u""
IN_MESSAGE_50 = u""
IN_MESSAGE_10 = u""
IN_MESSAGE_5 = u""
IN_MESSAGE_1 = u""
IN_MESSAGE_CONTAINER = u""

OUT_MESSAGE_100 = u""
OUT_MESSAGE_50 = u""
OUT_MESSAGE_10 = u""
OUT_MESSAGE_5 = u""
OUT_MESSAGE_1 = u""
OUT_MESSAGE_TOTAL = u"over"

print(WELCOME_MESSAGE)
container_weight = input(IN_MESSAGE_CONTAINER)
total_weight_100 = input(IN_MESSAGE_100)
total_weight_50 = input(IN_MESSAGE_50)
total_weight_10 = input(IN_MESSAGE_10)
total_weight_5 = input(IN_MESSAGE_5)
total_weight_1 = input(IN_MESSAGE_1)
value_100 = int(round((total_weight_100 - container_weight)/WEIGHT_100)) * 100
value_50 = int(round((total_weight_50 - container_weight)/WEIGHT_50)) * 50
value_10 = int(round((total_weight_10 - container_weight)/WEIGHT_10)) * 10
value_5 = int(round((total_weight_5 - container_weight)/WEIGHT_5)) * 5
value_1 = int(round((total_weight_1 - container_weight)/WEIGHT_1)) * 1
value_total = value_100 + value_50 + value_10 + value_5 + value_1
print(OUT_MESSAGE_100 + str(value_100))
print(OUT_MESSAGE_50 + str(value_50))
print(OUT_MESSAGE_10 + str(value_10))
print(OUT_MESSAGE_5 + str(value_5))
print(OUT_MESSAGE_1 + str(value_1))
print(OUT_MESSAGE_TOTAL + str(value_total))

