from django.shortcuts import render


# Create your views here.
def calc(request, x, action, y):
    res = 0
    symbol = ''
    err = ''
    if action == 'add':
        symbol = ' + '
        res = int(x + y)

    elif action == 'mult':
        symbol = '*'
        res = x * y

    elif action == 'div':
        symbol = '/'
        try:
            res = x / y
        except ZeroDivisionError:
            err = 'paraparapa'

    elif action == 'sub':
        symbol = '-'
        res = int(x - y)
        print(symbol)


    ren = f'{x} {symbol} {y} = {res}'
    return render(request, 'home.html', {'ren': ren, 'err': err})
