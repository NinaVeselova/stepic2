# https://stepik.org/lesson/24461/step/9?unit=6767
class Buffer:
    def __init__(self):
        self.buff = []

    def add(self, *a):
        for i in a:
            self.buff.append(i)
            if len(self.buff) == 5:
                print(sum(self.buff))
                self.buff.clear()

    def get_current_part(self):
        return self.buff
