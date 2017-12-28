import random
import timeit


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






for trial in [2** _ for _ in range(1,6)]:
    num = [random.randint(1,99) for _ in range(trial)]
    mfast= timeit.timeit(stmt = 'uniquecheckfast(num)',setup= 'import random\nfrom __main__ import uniquecheckfast\nnum='+str(num))

    print('{0:d}\t{1:f}'.format(trial,mfast))

