# -*- coding: utf-8 -*-
"""
@author:xuyuntao
@time:2020/10/19:9:47
@email:xuyuntao@189.cn
"""
"""使用模拟退火算法进行有干扰对的频率分配，需已知干扰对、用户数、可用频率，
暂时只能求解该可用频率情况下的最优频率分配，求解最小使用频率需不断修改可用频率数"""
import numpy
from freqCal import *
from s100p2588 import intference_data

stationsNum=100                                                        # 总台站数
freqNum=20                                                             # 给定频点个数
intfereArr=numpy.zeros([stationsNum,stationsNum],dtype=numpy.bool)     # 初始化干扰对矩阵
for _ in intference_data:                                              # 根据数据生成干扰对矩阵
    intfereArr[_[0], _[1]] = True
    intfereArr[_[1], _[0]] = True
freqAssign=numpy.zeros(stationsNum,dtype=numpy.int32)                  # 初始化频率分配矩阵

T_max=8             # 最大温度
T_min=0.005# 1/freqNum # （1/freqNum适用于getFreqAssign，现不使用）     # 最小温度
L=5*stationsNum     # 一个温度循环次数
T_down_rate=0.8     # 降温速率

def getFreqAssign(FA, changeN, freqNum, T, stationsNum):
    """现不使用！！！
    在原有频率分配表基础上对一个台站的频率进行扰动，扰动幅度按T改变。
    FA为基础频率分配表
    changeN为修改频点位置
    freqNum为总共频率数
    T为当前温度
    stationsNum为台站数，应等于FANew.shape[0]"""
    u=numpy.random.randint(-freqNum*T,freqNum*T,size=1)
    FANew = FA.copy()
    FANew[changeN%stationsNum] += u[0]
    return (FANew % freqNum)

def getFreqAssign_2(FA, changeN, freqNum, stationsNum):
    """在原有频率分配表基础上对一个台站的频率进行改动，改动范围始终为[0,freqNum]。
    FA为基础频率分配表
    changeN为修改频点位置
    freqNum为总共频率数
    stationsNum为台站数，应等于FANew.shape[0]"""
    u=numpy.random.randint(0,freqNum,size=1)
    FANew = FA.copy()
    FANew[changeN%stationsNum] = u[0]
    return (FANew % freqNum)

bestFreqAssign = freqAssign                                 # 最优频率分配矩阵
bestInterfereNum = intfereNum(intfereArr, bestFreqAssign)   # 最优干扰对数
T = T_max                                                   # 温度 初始设为最大温度
iterCycle = 0                                               # 当前循环次数
bestFreqAssignGen, bestInterfereNumGen = [bestFreqAssign], [bestInterfereNum]    # 记录


bestFreqAssignNow, bestInterfereNumNow = bestFreqAssign, bestInterfereNum
while True:
    print("当前最小干扰对数:", bestInterfereNum)
    for i in range(L):
        # FA = getFreqAssign(bestFreqAssignNow, i, freqNum, T, stationsNum)
        FA = getFreqAssign_2(bestFreqAssignNow, i, freqNum, stationsNum)
        IN = intfereNum(intfereArr, FA)

        freqUsage=freqUsageCal(freqNum, bestFreqAssign)
        # Metropolis
        df = IN - bestInterfereNumNow
        if df <= 0 or numpy.exp(-df / T) > numpy.random.rand():
            bestFreqAssignNow, bestInterfereNumNow = FA, IN
            if (IN < bestInterfereNum):
                bestFreqAssign, bestInterfereNum = FA, IN
                print("当前最小干扰对数:", bestInterfereNum)

    iterCycle += 1
    print("大循环次数:", iterCycle,"，当前温度:",T,"，最小温度:",T_min)
    T = T * T_down_rate
    bestInterfereNumGen.append(bestInterfereNum)
    bestFreqAssignGen.append(bestFreqAssign)

    if bestInterfereNum<=0:
        stop_code = "找到最优结果。"
        break

    if T < T_min:
        stop_code = "冷却到最小温度。"
        break


print("--------------------结果-------------------")
print(stop_code)
print("频率分配表:", bestFreqAssign, "\n干扰对数:", bestInterfereNum, "\n频点使用数:", freqUsageCal(freqNum, bestFreqAssign))