import os
from module.Student import Student

folderPath = os.path.join(os.getcwd(), 'data')
filePath = os.path.join(folderPath, 'stu.txt')

allStus = []


def initData():
    stus = []
    if not os.path.exists(folderPath):
        os.makedirs(folderPath)
    if not os.path.isfile(filePath):
        with open(filePath, 'w') as f:
            f.write('')
    with open(filePath, 'r') as f:
        stus = [Student(*stu.replace('\n', '').split(',')) for stu in filter(lambda line: line != '\n', f.readlines())]
    return stus


# 重写整个数据文件
def flushAllStus():
    with open(filePath, 'w') as f:
        f.write('\n'.join([*[stu.toFileString() for stu in allStus], '']))


# 查找学生数据
def findStudentIndex(stuno, callback):
    allStuNos = [stu.no for stu in allStus]
    if stuno in allStuNos:
        return callback(allStuNos.index(stuno))
    else:
        print(f'未找到学生编号为{stuno}的学生信息')


# 查找学生数据
def queryStudent(stuno):
    return allStus if stuno == '' else [findStudentIndex(stuno, lambda index: allStus[index])]


def updateStudent(stu, isAdd):
    if not isAdd:
        delStudent(stu.no)
    # 将数据添加到内存中
    allStus.append(stu)
    # 修改数据文件
    with open(filePath, 'a') as f:
        f.write(f'{stu.toFileString()}\n')


def __delStudent__(index):
    allStus.pop(index)
    flushAllStus()
    return 1


def delStudent(stuno):
    return findStudentIndex(stuno, __delStudent__)


def sortStudent(sortKey):
    global allStus
    allStus = sorted(allStus, key=lambda item: int(getattr(item, sortKey)))
    flushAllStus()
    Student.allStus = allStus


def getAllStudent():
    return allStus


allStus = initData()

Student.allStus = allStus
