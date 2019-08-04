# https://stepik.org/lesson/24464/step/4?unit=6769
class multifilter:
    def judge_half(pos, neg):
        if pos >= neg:
            return True
        else:
            return False

    def judge_any(pos, neg):
        if pos >= 1:
            return True
        else:
            return False

    def judge_all(pos, neg):
        if neg == 0:
            return True
        else:
            return False

    def posneg(self):
        pos = 0
        neg = 0
        for j in self.funcs:
            if j(self.iterable[self.i]):
                pos += 1
            else:
                neg += 1
        return pos, neg

    def __init__(self, iterable, *funcs, judge=judge_any):
        self.iterable = iterable
        self.funcs = funcs
        self.judge = judge
        self.i = 0
        self.k = len(iterable)

    def __iter__(self):
        return self

    def __next__(self):
        while self.i < self.k:
            z = self.posneg()
            if self.judge(z[0], z[1]):
                self.i += 1
                return self.iterable[self.i - 1]
            else:
                self.i += 1
        raise StopIteration
