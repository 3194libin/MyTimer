import time as t


class MyTimer:

    def __str__(self):
        return self.prompt

    __repr__ = __str__

    def start(self):
        self.start = t.localtime()
        print('计时开始。。。')

    def stop(self):
        self.stop = t.localtime()
        self.calc()
        print('计时结束！')

    def calc(self):
        self.lasted = []
        self.prompt = '总共运行了'
        for index in range(6):
            self.lasted.append(self.stop[index] - self.start[index])
            self.prompt += str(self.lasted[index])

