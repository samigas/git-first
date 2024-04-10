name = input('hin/her name')
def Hello_n(prompt):
    msg1 = 'Hellow ' + prompt
    msg2 = 'welcome to seoul'
    N1 = len(msg1)
    N2 = len(msg2)
    nstr = len(msg1) if (len(msg1) > len(msg2)) else len(msg2)
    print('-' * nstr)
    print(msg1)
    print(msg2)
    print('-' * nstr)

Hello_n(name)
