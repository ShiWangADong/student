from manage.common.ActionItem import ActionItem
from manage.module.Student import Student
from manage.data.Student import sortStudent, getAllStudent


# 添加学生
def sortFunc(sortKey):
    sortStudent(sortKey)
    print('排序完成结果为：')
    print('编号\t\t姓名\t\t年龄\t\t分数')
    for stu in getAllStudent():
        print(stu)


childrenAction = [ActionItem(str(index + 1), item['name'], lambda item=item: sortFunc(item['key'])) for index, item in
                  enumerate(Student.getSortableAttrs())]

sortAction = ActionItem('5', '排序学生', childrenAction, prompt='排序类型')
