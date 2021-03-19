from common.ActionItem import ActionItem
from module.Student import Student
from data.Student import queryStudent


# 添加学生
def query():
    stus = queryStudent(Student.getInputStuno(False, True))
    print('查询结果为：')
    print('编号\t\t姓名\t\t年龄\t\t分数')
    for stu in stus:
        print(stu)


queryAction = ActionItem('4', '查找学生信息', query)
