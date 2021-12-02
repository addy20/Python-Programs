# Example 3

# a=6
# def f():
#     a=5
#     def g():
#         b=a
#         print('Inside function g, b: ',b)
#     g()
# f()   

# Example 4
def f():
    def g():
        a=5
    g()
    print('in outer function g, a=',a)
f()        