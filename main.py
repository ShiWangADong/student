from manage.common.ActionItem import ActionItem
from manage.control.Delete import deleteAction
from manage.control.Query import queryAction
from manage.control.Update import addAction, editAction
from manage.control.Sort import sortAction


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
