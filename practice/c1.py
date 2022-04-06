class Student():
    sum =0
    def __init__(self,name,age):
        #初始化对象的属性
        self.name = name
        self.age =age
        print(self.name)
        # self.__class__.sum += 1
        # print('当前班级学生总数为：' + str(self.__class__.sum))

    def __marking(self,score):
        if score < 0:
            return '不能够给别人打负分'
        self.score = score
        print(self.name + '同学本次分数为' + str(self.score))
    # def do_homework(self):
    #     pass
    # @classmethod
    # def plus_sum(cls):
    #     cls.sum += 1
    #     print(cls.sum)

    # @staticmethod
    # def add(x,y):
    #     pass
student1 = Student('tom',20)
result = student1.__marking(70)
print(result)
# student2 = Student('jerry',5)
