#!/usr/bin/env python
# -*- encoding: UTF-8 -*-
WEIGHT_100 = 8.5
WEIGHT_50 = 8.25
WEIGHT_10 = 6.9
WEIGHT_5 = 6.5
WEIGHT_1 = 4.5

WELCOME_MESSAGE = u"Athugið að þetta forrit tekur allar upplýsingar inn sem tölur í grömmum. t.d skal tákna 4 kíló og 350 grömm sem 4350"
IN_MESSAGE_100 = u"Stimplið inn þyngd Hundraðkallanna\n"
IN_MESSAGE_50 = u"Stimplið inn þyngd fimmtíukallanna\n"
IN_MESSAGE_10 = u"Stimplið inn þyngd tíkallanna\n"
IN_MESSAGE_5 = u"Stimplið inn þyngd fimmkallanna\n"
IN_MESSAGE_1 = u"Stimplið inn þyngd einakrónanna\n"
IN_MESSAGE_CONTAINER = u"Stimplið inn þyngd ílatsins sem klinkið var vigað í, sláið inn 0 ef þetta á ekki við\n"

OUT_MESSAGE_100 = u"Heildarvirði hundraðkallanna: "
OUT_MESSAGE_50 = u"Heildarvirði fimmtíukallanna: "
OUT_MESSAGE_10 = u"Heildarvirði tíkallanna: "
OUT_MESSAGE_5 = u"Heildarvirði fimmkallanna: "
OUT_MESSAGE_1 = u"Heildarvirði einakrónanna: "
OUT_MESSAGE_TOTAL = u"Heildarvirði: "

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

