# -*- coding: cp936 -*-
from math import *
import random as rd
from s100p2588 import intference_data
import numpy
from freqCal import intfereNum
from freqCal import freqUsageCal

stationsNum=100
freqNum=40


intfereArr=numpy.zeros([stationsNum,stationsNum],dtype=numpy.bool)
for _ in intference_data:
    intfereArr[_[0], _[1]] = True
    intfereArr[_[1], _[0]] = True
freqAssign=numpy.zeros(stationsNum,dtype=numpy.float32)
# intfereCouple_0,intfereCouple_1=numpy.where(intfereArr==True)
# intfereFreq_0=freqAssign[intfereCouple_0]
# intfereFreq_1=freqAssign[intfereCouple_1]
# intfereNum=int((intfereFreq_0==intfereFreq_1).sum()/2)

# for i in range(10000):
#     freqAssign=numpy.random.randint([freqNum]*stationsNum)#numpy.random.random(5)#list(rd.randint(0,frequencies-1) for m in range(stations))
#     if intfereNum(intfereArr, freqAssign)==0:
#         break


print('ָ�䷽����'+str(freqAssign))
print("ʹ��Ƶ����",freqUsageCal(freqNum,freqAssign))
# print('���������'+str(i+1))
print('���Ŷԣ�' + str(intfereNum(intfereArr, freqAssign)))