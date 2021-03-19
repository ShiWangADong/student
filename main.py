from common.ActionItem import ActionItem
from control.Delete import deleteAction
from control.Query import queryAction
from control.Update import addAction, editAction
from control.Sort import sortAction


# 主函数
def main():
    mainAction = ActionItem('', '', [addAction, editAction, deleteAction, queryAction, sortAction],
                            footerTip=''.center(34, '-'),
                            headerTip='学生管理系统'.center(30, '-'), prompt='功能菜单', isMain=True)
    ActionItem.mainAction = mainAction
    mainAction.start()


# 增加调用main()函数
if __name__ == '__main__':
    main()
