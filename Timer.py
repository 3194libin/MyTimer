import time as t

class MyTimer:

    def __init__(self):
        self.unit = ['年','月','天','时','分','秒']
        self.prompt = '未开始计时'
        self.lasted = []
        self.begin = 0
        self.end = 0

    def __str__(self):
        return self.prompt

    __repr__ = __str__

    def start(self):
        self.begin = t.localtime()
        print('计时开始。。。')

    def stop(self):
        self.stop = t.localtime()
        self.calc()
        print('计时结束！')

    def calc(self):
        self.lasted = []
        self.prompt = '总共运行了'
        for index in range(6):
            self.lasted.append(self.stop[index] - self.begin[index])
            if self.lasted[index]:
                self.prompt += str(self.lasted[index])+self.unit[index]