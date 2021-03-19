# 循环输入，直到返回正确结果
def loopInput(prompt, validate=False, actions=[], headerTip='', footerTip=''):
    validate = validate if validate else lambda val, *args: '' if val != '' else f'{prompt}不能为空'
    while True:
        inputPrompt = f'请输入{prompt}：'
        if footerTip != '':
            inputPrompt = '\n'.join([footerTip, inputPrompt])
        actionsIndexArray = []
        if len(actions) > 0:
            actionsIndexArray = [item.index for item in actions]
            inputPrompt = '\n'.join([*[action.tostring() for action in actions], inputPrompt])
        if headerTip:
            print(headerTip)
        value = input(inputPrompt)
        # 注入action功能
        if len(actions) > 0:
            if value in actionsIndexArray:
                actionItem = actions[actionsIndexArray.index(value)]
                actionItem.start()
                break
        msg = validate(value, actionsIndexArray)
        if msg == '':
            return value
        elif type(msg) == str:
            print(msg)
        elif hasattr(msg, '__call__'):
            msg()
            break


# 判断字符串是否为空
def isNull(value):
    return value == ''
