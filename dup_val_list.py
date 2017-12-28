import timeit
import random
def uniquecheckfast(alist):

  # Return true if alist contains any duplicates. 
  # it completes in O(n) time with O(n) space required.
  # Individual elements must be hashable. 

    check = set()
    for v in alist:
         if v in check:
             return True
         check.add(v)
    return False

def uniquecheckslow(alist):
    ''' return true if alist contains ant duplicate.
        Completes in O(n^2) time with no space required
     '''

    for i in range(len(alist)-1):
        for j in range(i+1,len(alist)):
            if alist[i] == alist[j]:
                return True
    return False


print('N\tSlow     \tFast')   

for trial in [2** _ for _ in range(1,7)]:
    numbers = [random.random() for _ in range(trial)]
    mSlow = timeit.timeit(stmt = 'uniquecheckslow(numbers)',setup='import random\nfrom __main__ import uniquecheckslow\nnumbers = '+str(numbers),number=1000)
    mFast = timeit.timeit(stmt = 'uniquecheckfast(numbers)',setup='import random\nfrom __main__ import uniquecheckfast\nnumbers = '+str(numbers),number = 1000)
    print('{0:d}\t{1:f}\t{2:f}'.format(trial,mSlow,mFast))
    
         
        