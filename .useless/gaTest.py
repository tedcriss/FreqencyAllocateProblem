# -*- coding: utf-8 -*-
"""
@author:xuyuntao
@time:2020/10/19:9:50
@email:xuyuntao@189.cn
"""
import numpy
import geatpy as ea   # import geatpy
from gaFreqAssignProblem import FreqAssignProblem # 导入自定义问题接口
from s100p2588 import intference_data


if __name__ == '__main__':
    stationsNum = 100
    freqNum = 100

    intfereArr = numpy.zeros([stationsNum, stationsNum], dtype=numpy.bool)
    for _ in intference_data:
        intfereArr[_[0], _[1]] = True
        intfereArr[_[1], _[0]] = True

    """================================实例化问题对象==========================="""
    problem = FreqAssignProblem(stationsNum,intfereArr,freqNum) # 生成问题对象
    """==================================种群设置==============================="""
    Encoding = 'RI'       # 编码方式
    NIND = 50             # 种群规模
    Field = ea.crtfld(Encoding, problem.varTypes, problem.ranges, problem.borders) # 创建区域描述器
    population = ea.Population(Encoding, Field, NIND) # 实例化种群对象（此时种群还没被初始化，仅仅是完成种群对象的实例化）
    """================================算法参数设置============================="""
    myAlgorithm = ea.soea_SEGA_templet(problem, population) # 实例化一个算法模板对象
    myAlgorithm.MAXGEN = 100000 # 最大进化代数
    myAlgorithm.mutOper.Pm = 0.5 # 变异概率
    myAlgorithm.drawing = 2 # 设置绘图方式（0：不绘图；1：绘制结果图；2：绘制目标空间过程动画；3：绘制决策空间过程动画）
    """===========================调用算法模板进行种群进化======================="""
    [population, obj_trace, var_trace] = myAlgorithm.run() # 执行算法模板
    population.save() # 把最后一代种群的信息保存到文件中
    # 输出结果
    # best_gen = np.argmin(problem.maxormins * obj_trace[:, 1]) # 记录最优种群个体是在哪一代
    # best_ObjV = obj_trace[best_gen, 1]
    # print('最优的目标函数值为：%s'%(best_ObjV))
    # print('最优的决策变量值为：')
    # for i in range(var_trace.shape[1]):
    #     print(var_trace[best_gen, i])
    # print('有效进化代数：%s'%(obj_trace.shape[0]))
    # print('最优的一代是第 %s 代'%(best_gen + 1))
    # print('评价次数：%s'%(myAlgorithm.evalsNum))
    # print('时间已过 %s 秒'%(myAlgorithm.passTime))
