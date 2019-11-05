# 1'den N'e kadar olan sayıların toplanması
def toplama(n) :
    if n == 0 :
        return 0
    return n + toplama(n-1)
    print(toplama(n))
