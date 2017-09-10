#-*- coding: utf-8 -*-
import matplotlib.pyplot as plt
from random import choice
class RandomWalk():
    """一个生成随机漫步数据的类"""

    def __init__(self, num_points=5000):
        """初始化随机漫步的属性"""
        self.num_points = num_points

        #所有随机漫步都始于（0,0）
        self.x=[0]
        self.y=[0]

    def fill_walk(self):
        """计算随机漫步包含的所有点"""

        #不断的漫步，直到列表达到指定的长度
        while len(self.x) < self.num_points:
            next_x = self.x[-1]+self.get_step()
            next_y = self.y[-1]+self.get_step()

            # 拒绝原地踏步
            if self.get_step()=='0':
                continue

            self.x.append(next_x)
            self.y.append(next_y)

    def get_step(self):
            #决定前进方向以及沿这个方向前进的距离
            direction = choice([1, -1])
            distance = choice([0, 1, 2, 3, 4])
            step = direction * distance
            return (step)

while True:
    rw = RandomWalk(2)
    rw.fill_walk()
    plt.figure(figsize=(10, 6))
    point_numbers = list(range(rw.num_points))
    plt.title("随机漫步", fontsize=30, fontproperties='SimHei')
    plt.plot(rw.x, rw.y, linewidth=1)
    plt.scatter(0,0,edgecolors='none',c='green', s=100)
    plt.scatter(rw.x[-1], rw.y[-1], edgecolors='none',c='blue' , s=100)
    plt.show()

    keep_runnig = input("Make another walk? (y/n):")
    if keep_runnig == 'n':
        break