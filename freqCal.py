# -*- coding: utf-8 -*-
"""
@author:xuyuntao
@time:2020/10/19:9:44
@email:xuyuntao@189.cn
"""
import numpy

def intfereNum(intfereArr, freqAssign):
    """输入intfereArr，freqAssign"""
    intfereCouple_0, intfereCouple_1 = numpy.where(intfereArr == True)
    intfereFreq_0 = freqAssign[intfereCouple_0]
    intfereFreq_1 = freqAssign[intfereCouple_1]
    if not ((intfereFreq_0 == intfereFreq_1).sum() % 2 ==0):
        raise ValueError
    intfereNum = int((intfereFreq_0 == intfereFreq_1).sum() / 2)
    return intfereNum

def freqUsageCal(freqNum,freqAssign):
    if (freqAssign.max()<=freqNum):
        freqUsage=numpy.zeros(freqNum,dtype=numpy.bool)
        freqUsage[freqAssign.astype(numpy.int32)]=True
        return freqUsage.sum()
    else:
        raise ValueError
