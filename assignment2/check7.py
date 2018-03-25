import sys
import string

def truncate(f, n):
    '''Truncates/pads a float f to n decimal places without rounding'''
    s = '{}'.format(f)
    if 'e' in s or 'E' in s:
        return '{0:.{1}f}'.format(f, n)
    i, p, d = s.partition('.')
    return '.'.join([i, (d+'0'*n)[:n]])


for line in sys.stdin:
    key,val = line.split('\t')
    num1,num2 = val.split(', ')
    print('{0:d}\t{1:.1f}, {2:.1f}'.format(int(key),float(truncate(float(num1),1)),float(truncate(float(num2),1))))
