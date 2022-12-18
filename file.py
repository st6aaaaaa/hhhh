def func(*args):
    print( all( a> 0 for a in args) )

func(1,2,3,0)

