from manage.common.Tools import *
from manage.common.ActionItem import ActionItem, exitAction


class Student:
    allStus = []

    def __init__(self, no, name, age, score):
        self.no = no
        self.name = name
        self.age = age
        self.score = score

    def __str__(self):
        return f'{self.no}\t\t{self.name}\t\t{self.age}\t\t{self.score}'

    def toFileString(self):
        return f'{self.no},{self.name},{self.age},{self.score}'

    @staticmethod
    def getSortableAttrs():
        return [{'key': 'age', 'name': '年龄'}, {'key': 'score', 'name': '分数'}]

    @classmethod
    # 验证学号
    def validateNo(cls, no, isAdd=True, isAllowNull=False):
        stuNos = [stu.no for stu in cls.allStus]
        if isAllowNull and no == '':
            return no
        if isNull(no):
            return '学号不能为空'
        elif isAdd and no in stuNos:
            return f'学号[{no}]已经存在，请重新输入'
        elif not isAdd and no not in stuNos:
            return f'学号[{no}]不存在，请重新输入'
        else:
            return ''

    @classmethod
    def getInputStuno(cls, isAdd=True, isAllowNull=False):
        if not isAdd and len(cls.allStus) == 0:
            print('还没有录入学生信息')
            ActionItem.mainAction.start()
        else:
            return ActionItem('', '', [], validate=lambda value, *args: cls.validateNo(value, isAdd, isAllowNull),
                              prompt=f'学生编号{"(空表示所有)" if isAllowNull else ""}').start()

    @classmethod
    def createStudent(cls, isAdd):
        no = cls.getInputStuno(isAdd)
        attrs = {}
        for attr in [{'key': 'name', 'name': '姓名'}, {'key': 'age', 'name': '年龄'}, {'key': 'score', 'name': '分数'}]:
            attrs[attr['key']] = ActionItem('', '', [], validate=False,
                                            prompt=f'学生{attr["name"]}').start()
        return Student(no, **attrs)
