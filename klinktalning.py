#!/usr/bin/env python
# -*- coding: utf-8 -*-
import os
import sys
reload(sys)
sys.setdefaultencoding('utf-8')
try:
    os.system("chcp 65001")
    os.system("cls")
except:
    raise
WEIGHT_100 = 8.5
WEIGHT_50 = 8.25
WEIGHT_10 = 6.9
WEIGHT_5 = 6.5
WEIGHT_1 = 4.5


WELCOME_MESSAGE = u"Athugið að þetta forrit tekur allar upplýsingar inn sem eina tölu sem táknar grammafjölda. t.d skal stimpla inn 4 kíló og 350 grömm sem töluna 4350".encode('utf-8')
IN_MESSAGE_100 = u"Stimplið inn þyngd Hundraðkallanna\n".encode('utf-8')
IN_MESSAGE_50 = u"Stimplið inn þyngd fimmtíukallanna\n".encode('utf-8')
IN_MESSAGE_10 = u"Stimplið inn þyngd tíkallanna\n".encode('utf-8')
IN_MESSAGE_5 = u"Stimplið inn þyngd fimmkallanna\n".encode('utf-8')
IN_MESSAGE_1 = u"Stimplið inn þyngd einakrónanna\n".encode('utf-8')
IN_MESSAGE_CONTAINER = u"Stimplið inn þyngd ílátsins sem klinkið var vigað í, sláið annars inn 0 ef þetta á ekki við\n".encode('utf-8')
LINE = u"------------------------------------------------------\n".encode('utf-8')

OUT_MESSAGE_100 = u"Heildarvirði hundraðkallanna: ".encode('utf-8')
OUT_MESSAGE_50 = u"Heildarvirði fimmtíukallanna: ".encode('utf-8')
OUT_MESSAGE_10 = u"Heildarvirði tíkallanna: ".encode('utf-8')
OUT_MESSAGE_5 = u"Heildarvirði fimmkallanna: ".encode('utf-8')
OUT_MESSAGE_1 = u"Heildarvirði einakrónanna: ".encode('utf-8')
OUT_MESSAGE_TOTAL = u"Heildarvirði: ".encode('utf-8')


print(WELCOME_MESSAGE)
print(LINE)
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
raw_input()
