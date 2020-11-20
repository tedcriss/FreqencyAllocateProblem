# -*- coding: utf-8 -*-
"""
@author:xuyuntao
@time:2020/10/19:10:07
@email:xuyuntao@189.cn
"""
import numpy
import geatpy as ea
from freqCal import intfereNum

class FreqAssignProblem(ea.Problem): # 继承Problem父类
    def __init__(self , stationNum ,intfereArr , freqNum=30):
        name = 'FreqAssignProblem' # 初始化name（函数名称，可以随意设置）
        M = 1 # 初始化M（目标维数），单目标优化，要求使用频率数最少
        maxormins = [1] # 初始化maxormins（目标最小最大化标记列表，1：最小化该目标；-1：最大化该目标）
        Dim = stationNum # 初始化Dim（决策变量维数），
        varTypes = [1] * Dim # 初始化varTypes（决策变量的类型，元素为0表示对应的变量是连续的；1表示是离散的）
        lb = [0]*Dim # 决策变量下界
        ub = [freqNum-1]*Dim # 决策变量上界
        lbin = [1]*Dim # 决策变量下边界（0表示不包含该变量的下边界，1表示包含）
        ubin = [1]*Dim # 决策变量上边界（0表示不包含该变量的上边界，1表示包含）
        self.freqNum=freqNum
        self.intfereArr=intfereArr
        # 调用父类构造方法完成实例化
        ea.Problem.__init__(self, name, M, maxormins, Dim, varTypes, lb, ub, lbin, ubin)

    def aimFunc(self, pop): # 目标函数
        Vars = pop.Phen.astype(numpy.int32) # 得到决策变量矩阵
        freqUsage=numpy.zeros([Vars.shape[0],self.freqNum],dtype=numpy.bool)
        CV=numpy.zeros([Vars.shape[0],1],dtype=numpy.int32)
        for _ in range(Vars.shape[0]):
            freqUsage[_,Vars[_,:]]=True
            CV[_,0]=intfereNum(self.intfereArr, Vars[_])
        pop.ObjV=freqUsage.sum(axis=1).reshape([Vars.shape[0],1])
        # print(pop.ObjV)
        # 采用可行性法则处理约束
        pop.CV = CV
        print(CV)

    # def calReferObjV(self): # 设定目标数参考值（本问题目标函数参考值设定为理论最优值）
    #     referenceObjV = numpy.array([[20]])
    #     return referenceObjV