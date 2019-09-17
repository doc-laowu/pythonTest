from enum import Enum


class Student(object):

    __slots__ = ('__name', '__score') # 用tuple定义允许绑定的属性名称

    def __init__(self, name, score):
        # start with the '__' represent this is a private member variable value
        self.__name = name
        self.__score = score

    def print_score(self):
        print('%s: %s' % (self.__name, self.__score))


if __name__ == "__main__":

    Month = Enum('Month', ('Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec'))

    print(Month._member_map_.get("Jan"))

    s = Student("Tom", 234)
    s.print_score()