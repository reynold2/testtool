
# def d_args(args="1"):
#     def function(*args,**kwargs):
#         print("11")
#         def fun(*args,**kwargs):
#             x=WebTestCase()
#             return x
#         return fun
#     return function
# def wrapper(param):        # param = 'boss'
#     def wrapper_fun(fun):  # fun = fun1/fun2
#         def inner(*args,**kwargs):
#             print(' %s say：' % param)
#             WebTestCase(*args,**kwargs)
#         return inner
#     return wrapper_fun
# @wrapper(args="1")
# def WebTestCase(x):
#     x=x+1
#     return x
def wrapper(param="1"):        # pxaram = 'boss'
    def wrapper_fun(fun):  # fun = fun1/fun2
        def inner(*args,**kwargs):
            print(' %s say：' % param)
            return fun(*args,**kwargs)
        return inner
    return wrapper_fun

@wrapper('boss')  # fun1 = wrapper('boss')(fun1)
def fun1(*args,**kwargs):
    print('1!!')


# fun1()


class Testx(object):
    def __init__(self):
        self.x="ss"
        print("s")
    @wrapper(12)
    def pal(self,x):
        print(x)
        print("xxxx")
if __name__=="__main__":
    Testx().pal("22")