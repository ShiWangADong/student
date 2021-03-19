from sys import exit
from manage.common.Tools import loopInput


# 该类主要解决菜单的循环调用问题
class ActionItem:
    # 对应主方法
    mainAction = None

    # 构造方法
    def __init__(self, index, title, actions, prompt='', headerTip='', footerTip='', isMain=False,
                 validate=lambda startType, actionsIndexArray: f'您输入的序号不在范围{actionsIndexArray}内，请重新输入'):
        self.index = index
        self.title = title
        self.actions = actions
        self.headerTip = headerTip
        self.footerTip = footerTip
        self.prompt = prompt
        self.isMain = isMain
        self.validate = validate

    # 选中后的操作
    def start(self):
        # 如果传入的actions为数组，表示多级
        if type(self.actions) == list:
            tempActions = [*self.actions, ActionItem.getMenuAction(), exitAction]
            # 表示主菜单
            if self.isMain:
                tempActions.pop(-2)
            return loopInput(self.prompt, self.validate,
                             tempActions, headerTip=self.headerTip,
                             footerTip=self.footerTip)

        else:
            self.actions()
            self.mainAction.start()

    def __str__(self):
        return f'{self.index}、{self.title}'

    def tostring(self):
        return self.__str__()

    @classmethod
    def getMenuAction(cls):
        return ActionItem('9', '返回主菜单', cls.mainAction.start)


# 退出动作
exitAction = ActionItem('0', '退出系统', exit)
