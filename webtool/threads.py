def func_arg(arg =False,num=3):
    if arg:
        def func(funNume):
            print(funNume)
            def func_in(*args,**kargs):
                print(*args,**kargs)
                return funNume(*args,**kargs)
            return func_in
        return func
    else:
        def func(funNume):
            def func_in(*args,**kargs):
                return funNume(*args,**kargs)
            return func_in
        return func

# @func_arg(arg=True,num=2)
# def f1(a,b):
#     return 'haha'

