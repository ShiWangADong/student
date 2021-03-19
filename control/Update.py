from manage.common.ActionItem import ActionItem
from manage.module.Student import Student
from manage.data.Student import updateStudent


# 添加学生
def update(isAdd=True):
    newStu = Student.createStudent(isAdd)
    operator = '添加' if isAdd else '修改'
    updateStudent(newStu, isAdd)
    print(f'学生信息[{newStu.toFileString()}]已经{operator}成功')


# 新增信息
addAction = ActionItem('1', '录入学生信息', update)

# 编辑信息
editAction = ActionItem('2', '修改学生信息', lambda: update(False))
