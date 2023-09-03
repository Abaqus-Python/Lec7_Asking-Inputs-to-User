# ------------------------------------------------
from abaqus import *

num = getInput(prompt='Enter your age:\tPlease insert interger values only.', default='30')

try:
    int(num)
except:
    btn = getWarningReply(message='Age value is not valid!\nDo you want to use default value?',
            # buttons=(YES, NO))
            buttons=(CANCEL,))

    if btn == YES:
        num = '30'
    else:
        num = getInput(prompt='Enter your age:\tPlease insert interger values only.', default='30')
    print(num)

# fields = (('Enter your name:', ''),
            # ('Enter your age:\tPlease insert interger values only.', '30'))

# data = getInputs(fields=fields, label='Enter the details below:', dialogTitle='Basic Details')

# print(data)

# btn = getWarningReply(message='Age value is not valid!\nDo you want to use default value?',
            # buttons=(YES, NO))

# print(btn)


