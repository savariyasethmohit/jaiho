                                            # lambda function
# def cube(num):
#     return num+3                          # normal function
# print(cube(3))

# cube = lambda num:num**3
# print(cube(3))
#
# print((lambda num:num**3)(3))

# lst = ["james","king","anna","smith","lex"]
# lst.sort(key=len)
# print(lst)
#
# def lstchar(name):
#     return name[-1]
# lst.sort(key=lstchar)
# print(lst)

# lst.sort(key=lambda name:name[-1])
# print(lst)

                                       # fibnacci series
# def fibo(num):
#     if num in [0, 1]:
#         return num
#     return fibo(num-1)+fibo(num-2)
#
#
# for i in range(10):
#     print(fibo(i), end=" ")


def msg():
    return "hello world"

def makebold():
    def boldlogic():
        return "<b>"+msg()+"</b>"