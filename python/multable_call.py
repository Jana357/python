from kvr_exc import kvrmultable,kvrmultable_0

def multable(n):
    if (n<0):
        raise kvrmultable
    elif (n==0):
        raise kvrmultable_0
    else:
        for i in range(1,11):
            print("{} X {} = {}".format(n,i,n*i))
        else:
            print("-"*50)